from util.operation_excel import Operation_excel
from util.operation_json import operationJson
from data import data_config


class Get_data:

    def __init__(self,file_name=None,sheet_id=None):
        self.opera_excel=Operation_excel(file_name,sheet_id)

    #获取行数
    def get_base_lines(self):

        return self.opera_excel.get_lines()
    #获取 id
    def get_caseid(self,row):
        col=data_config.get_id()
        id=self.opera_excel.get_cell_value(row,col)
        return id

    #获取url
    def get_url(self,row):
        col=data_config.get_url()
        url=self.opera_excel.get_cell_value(row,col)
        return url

    #获取是否执行
    def get_is_run(self,row):
        col=data_config.get_run()

        run_model=self.opera_excel.get_cell_value(row,col)
        return run_model

    #是否携带header
    def is_header(self,row):
        col = data_config.get_header()

        header=self.opera_excel.get_cell_value(row, col)
        if header=="":
            return None
        else:
            return header

    # 获取请求方式
    def get_request_method(self, row):
        col = data_config.get_run_way()
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    #获取预期结果
    def get_expect_data(self,row):
        col = data_config.get_expect()
        expect= self.opera_excel.get_cell_value(row, col)
        if expect=="":
            return None
        return expect

    #获取请求数据
    def get_request_data(self,row):
        col=data_config.get_data()
        requeste_data=self.opera_excel.get_cell_value(row,col)

        if requeste_data=="":
            return None
        else:
            return requeste_data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self, row):
        opera_json = operationJson()
        req_data=self.get_request_data(row)
        if  req_data==None:
            return None
        else:
            req_data = opera_json.get_data(self.get_request_data(row))
            return req_data

     #通过获取header的关键字拿到对应的header的数据
    def get_headers_for_json(self, row):
        opera_json = operationJson()
        header_data=self.is_header(row)
        if header_data==None:
            return None
        else:
            req_data = opera_json.get_data(self.is_header(row))
        return req_data

    #写入数据
    def write_value(self,row,value):
        col=data_config.get_resule()
        self.opera_excel.write_data(row,col,value)



    #获取是否有数据依赖
    def  is_depend(self,row):
        col=data_config.get_case_dependent()

        case_depend=self.opera_excel.get_cell_value(row,col)
        if case_depend=="":
            return None
        else:
            return case_depend

     # 获取依赖数据的key

    def get_dependent_key(self, row):
        col = data_config.get_data_dependent()
        depent_key = self.opera_excel.get_cell_value(row, col)
        return depent_key

    #获取依赖的b接口中的key
    def  get_depent_files(self,row):
        col=data_config.get_file_dependent()
        fied_depend=self.opera_excel.get_cell_value(row,col)
        if fied_depend=="":
            return None
        else:
            return fied_depend

        # 获取是否有数据依赖
    def is_dependTwo(self, row):
        col = data_config.get_caseTwo_dependent()

        case_depend = self.opera_excel.get_cell_value(row, col)
        if case_depend == "":
            return None
        else:
            return case_depend

        # 获取依赖数据的key

    def get_Twodependent_key(self, row):
        col = data_config. get_dataTwo_dependent()
        depent_key = self.opera_excel.get_cell_value(row, col)
        return depent_key

    # 获取依赖的b接口中的key
    def get_Twodepent_files(self, row):
        col = data_config.get_fileTwo_dependent()
        fied_depend = self.opera_excel.get_cell_value(row, col)
        if fied_depend == "":
            return None
        else:
            return fied_depend


    #获取所依赖的headers的接口

    def is_dependCook(self, row):
        col = data_config.get_caseCookies_dependent()

        case_depend = self.opera_excel.get_cell_value(row, col)
        if case_depend == "":
            return None
        else:
            return case_depend

        # 获取所依赖的接口headers中的数据  比如接口a headers中的set-cookies

    def get_CookDependent_key(self, row):
        col = data_config.get_dataCookies_dependent()
        depent_key = self.opera_excel.get_cell_value(row, col)
        return depent_key

        # 获取依赖的b接口中的key

    def get_CookDepent_files(self, row):
        col = data_config.get_fileCookies_dependent()
        fied_depend = self.opera_excel.get_cell_value(row, col)
        if fied_depend == "":
            return None
        else:
            return fied_depend

    #获取接口中需要增加的随机值得字段
    def rdom(self,row):
        col = data_config.get_random_data()
        random_data = self.opera_excel.get_cell_value(row, col)
        if random_data == "":
            return None
        else:
            return random_data

    def get_dat_formata(self,row):
        col = data_config.get_data_formata()
        formata_data = self.opera_excel.get_cell_value(row, col)
        return  formata_data

    def except_mysql(self,row):
        col = data_config.get_mysql_expect()
        random_data = self.opera_excel.get_cell_value(row, col)
        if random_data == "":
            return None
        else:
            return random_data

    def get_sce_excepet(self,row):

        col = data_config.get_sencent_except()
        random_data = self.opera_excel.get_cell_value(row, col)
        if random_data == "":
            return None
        else:
            return random_data




if __name__=="__main__":
    g_data=Get_data(sheet_id=1)

    cerrent=g_data.get_CookDependent_key(2)

    a=g_data.get_Twodependent_key(2)

    print(a)






