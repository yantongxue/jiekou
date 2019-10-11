#coding=utf-8
import requests
import json
import pprint

from jsonpath_rw import jsonpath,parse





class RunMain:


 #data_formata是为了区分post中传参是data=data 这种形式还是json=data
    def send_post(self,url,data_formata=None,data=None,headers=None):

        if data_formata=="data":

            res = requests.post(url=url, data=data, headers=headers)

        else:
            res=requests.post(url=url,json=data,headers=headers)


        try:

            res_content=res.content.decode()
        except:
            res_content=res.content.decode('gbk')

        try:
            result=json.loads(res_content)
        except Exception:
            result=res_content

        res_header=res.headers
        # print (gzip.decompress(res).decode("utf-8"))
        return result,res_header



    def send_get(self,url,data_formata=None,data=None,headers=None):

        if data_formata=="data":
            res = requests.get(url=url, data=data, headers=headers, verify=False)
        else:

            res=requests.get(url=url,json=data,headers=headers,verify=False)

        try:
            result = json.loads(res.content.decode())

        except Exception:
            result = res.content.decode()

        res_header = res.headers

        return result,res_header



    def run_main(self,url,method,data_formata=None,data=None,headers=None):

        res=None
        if method=="post":
            res=self.send_post(url,data_formata,data,headers)
        else:
            res=self.send_get(url,data_formata,data=None,headers=None)
        return res


if __name__=="__main__":


    headers={
        "Content-Type":"application/json",
        "Cookie":"JSESSIONID=9HLSRWLkQFtYvDH6_BbOmkgxltV8oOg1Lhhw1A-x"

    }


    url="http://118.31.103.110/app/home/hot/list"



    run=RunMain()

    method="post"


    data1= {"checkType":0,"checkStats":"0","pageNum":1,"pageSize":10}

    res=requests.post(url,json=data1,headers=headers)

    result=res.content.decode()

    result=json.loads(result)

    print(result)


    json_exe = parse("$.data.list[*].id,phone")
    madle = json_exe.find(result)
    print("madle是%s" % madle)
    print ([math.value for math in madle])










    # data_formata="data"
    #
    # res=run.run_main(url,method,data_formata,data)
    # print(res[0])
    # print(res[1])



