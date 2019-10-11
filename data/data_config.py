#coding=utf-8
class global_var:
    #固定的列
    Id=0
    name=1
    url=2
    run=3
    request_way=4
    header=5
    case_depend=6
    data_depend=7
    filed_depend=8
    mys_data=9
    data=10
    expect=11
    mysql_expect = 12
    sencend_expect = 13
    resule=14



    case_depend_two=15
    data_depend_two=16
    file_depend_two=17

    data_formata=18

    case_depend_cookie = 19
    data_depend_cookie = 20
    file_depend_cookie = 21






#获取caseid
def get_id():
    return global_var.Id
def get_url():
    return global_var.url
def get_run():
    return global_var.run
def get_run_way():
    return global_var.request_way
def get_header():
    return global_var.header


def get_data():
    return global_var.data
def get_expect():
    return global_var.expect
def get_resule():
    return global_var.resule

def get_case_dependent():
    return global_var.case_depend
def get_data_dependent():
    return global_var.data_depend
def get_file_dependent():
    return global_var.filed_depend

def get_caseTwo_dependent():
    return global_var.case_depend_two
def get_dataTwo_dependent():
    return global_var.data_depend_two
def get_fileTwo_dependent():
    return global_var.file_depend_two

def get_caseCookies_dependent():
    return global_var.case_depend_cookie
def get_dataCookies_dependent():
    return global_var.data_depend_cookie
def get_fileCookies_dependent():
    return global_var.file_depend_cookie


def get_random_data():
    return global_var.mys_data

def get_data_formata():
    return global_var.data_formata


def get_mysql_expect():
    return global_var.mysql_expect
def   get_sencent_except():
    return global_var.sencend_expect




