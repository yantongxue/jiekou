#coding=utf-8
import unittest
import requests
import json
from base.demo import RunMain
import HTMLTestRunner


class Test_Method(unittest.TestCase):

    def test_01(self):
        url = "http://t.10jqka.com.cn/manage0033t/group/addGroup/"
        data = {
            "name": "ceshi",
            "ownerid": "359414791",
            "desc": "359414791",
            "numRes": "1000",
            "userRes": "2",
            "img": "http://u.thsi.cn/fileupload/data/Blog/2018/e43e707a38086e5f0925d26e5c33355e.jpg",
            "userResFile": "",

        }
        cookies = {

            "PHPSESSID": "khqqlip68b770d0ef53jnv6no4",
            "Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1": "1530598132",
            "Hm_lpvt_da7579fd91e2c6fa5aeb9d1620a9b333": "1530613727",
            "Hm_lvt_da7579fd91e2c6fa5aeb9d1620a9b333": "1530598132, 1530613727",
            "Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1": "1530613727",
            "v": "ArzNJ89Ey3OPOP8vW3IONGiSjVFttWDf4ll0o5Y9yKeKYVJHvsUwbzJpRDHl"
        }

        run=RunMain().run_main(url=url,method="post",data=data,headers=cookies)
        self.assertEqual(run["errorMsg"],'创建成功',"创建失败")
        globals()["errorMsg"]=run["errorMsg"]
        print (globals()["errorMsg"])

    @unittest.skip("test_02")
    def test_02(self):
        url = "http://t.10jqka.com.cn/manage0033t/group/addGroup/"

        data = {
            "name":globals()["errorMsg"] ,
            "ownerid": "359414791",
            "desc": "359414791",
            "numRes": "1000",
            "userRes": "2",
            "img": "http://u.thsi.cn/fileupload/data/Blog/2018/e43e707a38086e5f0925d26e5c33355e.jpg",
            "userResFile": "",

        }
        cookies = {

            "PHPSESSID": "khqqlip68b770d0ef53jnv6no4",
            "Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1": "1530598132",
            "Hm_lpvt_da7579fd91e2c6fa5aeb9d1620a9b333": "1530613727",
            "Hm_lvt_da7579fd91e2c6fa5aeb9d1620a9b333": "1530598132, 1530613727",
            "Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1": "1530613727",
            "v": "ArzNJ89Ey3OPOP8vW3IONGiSjVFttWDf4ll0o5Y9yKeKYVJHvsUwbzJpRDHl"
        }

        run = RunMain(url, method="post", data=data, cookies=cookies).res
        self.assertEqual(run["errorMsg"], '创建成功', "创建失败")




if __name__=="__main__":
    #filepath="../report/HtmlReport.html"
    #fp=open(filepath,"wb")
    # suite=unittest.TestSuite()
    # suite.addTest(Test_Method("test_01"))
    # suite.addTest(Test_Method("test_02"))


    #runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="this is first test")
    #runner.run(suite)
    # unittest.TextTestRunner().run(suite)
    b="6666666"
    print(globals())
    globals()["a"]=b
    print(globals())