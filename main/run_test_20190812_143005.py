#coding=utf-8
import os
import sys
sys.path.append("E:\\jiekou")
from data.get_data import Get_data
from base.demo import RunMain
from util.commen import CommonUtil

from data.dependdent_data import Deppenddent_data
from util.send_mail import SendMail
from redis import *
import json
from pymysql import *
from jsonpath_rw import jsonpath,parse
from util.operation_json import operationJson

class Run_Test():
    def __init__(self):
        with open("./sheet_id.conf","rb") as f:
            conf_info=eval(f.read())
        sheet_id=conf_info["sheet_id"]

        self.data=Get_data(sheet_id=sheet_id)

        self.run=RunMain()
        self.com_utl=CommonUtil()
        self.send=SendMail()




    def go_on_run(self):
        pass_count=[]
        fail_count=[]
        cow_count=self.data.get_base_lines()
        for i in range(1,cow_count):
            case=self.data.get_caseid(i)
            # print("case是%s"%case)
            url=self.data.get_url(i)
            # print("url是%s" % url)
            method=self.data.get_request_method(i)
            # print("method是%s" % method)
            data=self.data.get_data_for_json(i)
            # print("data是%s" % data)
            headers = self.data.get_headers_for_json(i)
            # print("headers是%s" % headers)
            expect=self.data.get_expect_data(i)
            # print("except是%s" % expect)
            is_run=self.data.get_is_run(i)
            dep_case=self.data.is_depend(i)
            dep_two=self.data.is_dependTwo(i)
            data_fmdat=self.data.get_dat_formata(i)
            dep_cookie=self.data.is_dependCook(i)
            mysql_expect=self.data.except_mysql(i)


            if is_run=="yes":
                if dep_case != None:
                    if method == "post":
                    # 自己根据redis解决依赖
                        self.depend_data = Deppenddent_data()
                        self.depend_data.redis_isIn(dep_case)
                        dep_value=self.depend_data.get_data_key(i)
                        # print(" dep_values是%s" %dep_value)
                        dep_key=self.data.get_depent_files(i)
                        # print(" dep_key是%s" % dep_key)
                        dp_case= dep_key.split(":")[0]
                        if dp_case=="data":
                            data[dep_key.split(":")[1]]=dep_value
                        else:
                            headers["Authorization"]="Bearer "+str(dep_value)
                        if dep_two!=None:
                            self.depend_data = Deppenddent_data()
                            self.depend_data.redis_isIn(dep_two)
                            dep_value = self.depend_data.get_data_twokey(i)
                            dep_key = self.data.get_Twodepent_files(i)
                            dep_len=len(dep_key.split(":"))
                            header_ordata = dep_key.split(":")[0]
                            #以下是为了解决a接中返回的值在b接口中是一一对应但不是这个值本身 比如false  在b接口中对应的是1 这样的关系
                            if header_ordata == "data":
                                if dep_len==2:
                                    data[dep_key.split(":")[1]] = dep_value
                                else:
                                    if  dep_value==False:
                                        dep_value = 1
                                    else:
                                        dep_value = 2
                                    data[dep_key.split(":")[1]] = dep_value
                            else:
                                headers["Authorization"] = "Bearer " + dep_value
                        if  dep_cookie!=None:
                            self.depend_data = Deppenddent_data()
                            self.depend_data.redis_isIn(dep_cookie)
                             # 获取所依赖的a接口headers中的value
                            dep_value = self.depend_data.get_data_keyCookie(i)
                            # 获取b接口中的key
                            dep_key = self.data.get_CookDepent_files(i)
                            # 将接口b headers中的dep_key=dep_value
                            headers[dep_key] = dep_value
                    #老师的方法解决依赖
                    # self.depend_data = Deppenddent_data(depent_case)
                    # depend_response_data = self.depend_data.get_data_for_key(i)
                    else:
                        self.depend_data = Deppenddent_data()
                        self.depend_data.redis_isIn( dep_case)
                        dep_value = self.depend_data.get_data_key(i)
                        url=url.format(dep_value)
                elif dep_cookie!=None:
                    self.depend_data = Deppenddent_data()
                    self.depend_data.redis_isIn(dep_cookie)
                    #获取所依赖的a接口headers中的value
                    dep_value = self.depend_data.get_data_keyCookie(i)
                    #获取b接口中的key
                    dep_key = self.data.get_CookDepent_files(i)
                    #将接口b headers中的dep_key=dep_value
                    headers[dep_key]=dep_value
                    # print("headers是%s" %headers)

                res=self.run.run_main(url,method,data_fmdat,data,headers)
                res_content=res[0]
                res_headers=res[1]
                res_content=json.dumps(res_content)
                src = StrictRedis()
                src.set(case,res_content)
                case_headers=case+":headers"
                src.set(case_headers,str(res_headers))
                res_content=json.loads(res_content)
                print(res_content)

                if self.com_utl.is_contain(expect,res_content):
                    #判断是否需要进行数据库中验证

                    mysql_curso = self.data.rdom(i)
                    # print("mysql_curso 是%s" %mysql_curso)
                    if mysql_curso==None:
                        self.data.write_value(i,"pass")
                        pass_count.append(i)
                    else:

                        conn = connect(host="47.98.179.27", port=3306, user="root", password="Jqdev.Com#123",
                                       database="shouji")
                        cs1 = conn.cursor()
                        count = cs1.execute(mysql_curso)

                        if count==int(mysql_expect):
                            self.data.write_value(i, "pass")
                            pass_count.append(i)
                        else:
                            self.data.write_value(i, count)
                            fail_count.append(i)

                else:
                    scend_except=self.data.get_sce_excepet(i)
                    if scend_except==None:
                        res_content=str(res_content)
                        self.data.write_value(i, res_content)
                        fail_count.append(i)
                    else:
                        if self.com_utl.is_contain(scend_except, res_content):
                            self.data.write_value(i, "pass")
                            pass_count.append(i)
                        else:
                            self.data.write_value(i, res_content)
                            fail_count.append(i)

        #self.send.send_main(pass_count,fail_count)


if __name__=="__main__":
    run=Run_Test()
    run.go_on_run()