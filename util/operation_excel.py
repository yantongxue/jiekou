#coding=utf-8
import xlrd
from xlutils.copy import copy




class Operation_excel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name=file_name

        else:
            self.file_name = "../datacofig/interface.xls"


        if sheet_id:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = 0

        self.data=self.get_data()

    def get_data(self):
        data=xlrd.open_workbook(self.file_name)
        table=data.sheets()[self.sheet_id]
        return table
    #获取单元格的行数
    def get_lines(self):
        return self.data.nrows
    #获取单元格的内容
    def  get_cell_value(self,row,col):
        return self.data.cell_value(row,col)
    #写入数据哦
    def write_data(self,row,col,value):
        read_data=xlrd.open_workbook(self.file_name)
        write_data=copy(read_data)
        sheet_data=write_data.get_sheet(self.sheet_id)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)




    #找到某一行的内容
    def get_row_data(self,row):
        rows=self.data.row_values(row)
        return rows

    #根据case_id找到对应行的num、
    def get_row_num(self,case_id):
        cols_data=self.get_col_data(0)
        num=int(0)
        for col_data in cols_data:
            if case_id in col_data:
                return  (num)
            else:
                num=int(num+1)



    #根据case_id找到对应行的内容
    def get_row_value(self,case_id):
        num=self.get_row_num(case_id)
        rows_data=self.get_row_data(num)
        return rows_data


    #找到某一列的内容、
    def  get_col_data(self,col_num):

        cols=self.data.col_values(col_num)
        return cols








if __name__=="__main__":
    op=Operation_excel()
    row_value=op.get_row_data(2)
    print(row_value)

