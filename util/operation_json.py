import json
import requests
class operationJson:
    def __init__(self):
        self.data=self.read_json()
    def read_json(self):
        with open("../datacofig/requser_data.json",'r',encoding="utf-8") as fp:#注意当json文件中有汉字的时候，要加上编码'r',encoding='UTF-8'
            data=json.load(fp)

            return data

    def get_data(self,id):
        return self.data[id]




if __name__=="__main__":
    op=operationJson()
    # print(op.read_json())
    # print(type(op.read_json()))
    print(op.get_data("setBlack6"))

