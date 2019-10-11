import csv
from tqdm import tqdm
from time  import sleep


def write_csv_files(path,headers,rows):
    with open(path,"a",encoding="utf-8",newline="")as f:
        f_csv=csv.DictWriter(f,headers)
        f_csv.writeheader()
        f_csv.writerows(rows)

def write_csv_headers(path,headers):
    with open(path,"a",encoding="utf-8",newline="")as f:
        f_csv=csv.DictWriter(f,headers)
        f_csv.writeheader()
def write_csv_row(path,headers,rows):
    with open(path,"a",encoding="gb18030",newline="")as f:
        f_csv=csv.DictWriter(f,headers)
        if type(rows)==type({}):
            f_csv.writerow(rows)
        else:
            f_csv.writerows(rows)

if __name__=="__main__":
    item = {'a': ["1","2"]}

    fieldnames = ['a']

    with open('test.csv', 'a') as f:
        f_csv =csv.DictWriter(f, fieldnames=fieldnames)
        f_csv.writeheader()
        f_csv.writerows(item)








