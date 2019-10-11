#coding=utf-8
from util.operation_excel import Operation_excel
from data.get_data import Get_data
from base.demo import RunMain
import json
from jsonpath_rw import jsonpath,parse
from redis import *
class Deppenddent_data:
    def __init__(self,):
        # self.case_id=case_id
        self.ope_excel=Operation_excel()

        with open("./sheet_id.conf","rb") as f:
            conf_info=eval(f.read())
        sheet_id=conf_info["sheet_id"]

        self.data=Get_data(sheet_id=sheet_id)

    # #根据case_id获取整行数据
    # def get_case_line_data(self):
    #     rows_data=self.ope_excel.get_row_value(self.case_id)
    #     return rows_data

     #根据行num执行依赖的接口
    def run_dependent(self,case_id):
        run=RunMain()
        row_num=self.ope_excel.get_row_num(case_id)
        url=self.data.get_url(row_num)
        method=self.data.get_request_method(row_num)
        request_data=self.data.get_data_for_json(row_num)
        headers=self.data.get_headers_for_json(row_num)
        res=run.run_main(url,method,request_data,headers)
        return res

    # 依赖的接口执行完之后，在依赖的接口返回数据中找到下个接口需要用的数据并且赋值给下个接口
    def get_data_for_key(self,row):
        dependent_data=self.data.get_dependent_key(row)
        print("dependent_data是%s" %dependent_data)
        print(type(dependent_data))
        dep_case_id=self.data.is_depend(row)
        print(dep_case_id)
        print(type(dep_case_id))
        response_data=self.run_dependent(dep_case_id)
        print("执行依赖接口的返回值是%s"%response_data)
        print(type(response_data))
        json_exe=parse(dependent_data)
        madle=json_exe.find(response_data)
        print("madle是%s"%madle)
        return[math.value for math in madle][0]

    def redis_isIn(self,case_id):
        src = StrictRedis()
        try:
            src.get(case_id)
        except:
            result=self.run_dependent(case_id)
            src.set(case_id, result)


    def  get_data_key(self,row):
        dependent_data = self.data.get_dependent_key(row)  # 结果是获取所要依赖的key 也就是a接口中字段的名字
        # print("a接口中的字段的名字是%s" %dependent_data)
        dep_case_id = self.data.is_depend(row)
        src = StrictRedis()
        response_data = src.get(dep_case_id)
        response_data = response_data.decode(encoding='utf-8')
        response_data = json.loads(response_data)
        # print("redis中的数据是%s" %response_data)
        json_exe = parse(dependent_data)
        madle = json_exe.find(response_data)
        depend_value = [math.value for math in madle][0]
        # print(depend_value)
        return depend_value


    def  get_data_twokey(self,row):
        dependent_data = self.data.get_Twodependent_key(row)  # 结果是获取所要依赖的key 也就是a接口中字段的名字
        # print("-a接口中的字段的名字是%s" %dependent_data)
        dep_case_id = self.data.is_dependTwo(row)
        src = StrictRedis()
        response_data = src.get(dep_case_id)
        response_data = response_data.decode(encoding='utf-8')
        response_data = json.loads(response_data)
        print("redis中的数据是%s" %response_data)
        json_exe = parse(dependent_data)
        madle = json_exe.find(response_data)
        depend_value = [math.value for math in madle][0]
        # print(depend_value)
        return depend_value


    #获取依赖的接口中的headers中的数据

    def get_data_keyCookie(self, row):

        dependent_data = self.data.get_CookDependent_key(row)  # 结果是获取所要依赖的key 也就是a接口中字段的名字
        # print("a接口中的字段的名字是%s" %dependent_data)
        dep_case_id = self.data.is_dependCook(row)
        # print("redis中依赖的字段是%s" %dep_case_id)
        src = StrictRedis()
        response_data = src.get(dep_case_id)
        response_data = response_data.decode()
        response_data = eval(response_data)
        json_exe = parse(dependent_data)
        madle = json_exe.find(response_data)
        depend_value = [math.value for math in madle][0]
        cookie=depend_value.split(";")[0]
        return cookie





if __name__=="__main__":


    dep=Deppenddent_data()
    res=dep.get_data_keyCookie(2)
    print(res)









