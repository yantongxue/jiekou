from requests.exceptions import RequestException
import requests
import re
from tqdm import tqdm
from time  import sleep
import csv
def get_on_page(url):




    try:
        response = requests.get(url)
        if response.status_code==200:
            return (response.text)
        return  None
    except RequestException as e:
        return None



def parse_one_page(html):
    pattern = re.compile('<div class="post-title">\\s+(.*?)</div>')  # 此处的\\s+代表空格
    items = re.findall(pattern, html)
    for item in items:
        Articles_title=item
        yield {
            "title": Articles_title
        }



def write_csv_files(path,headers,rows):
    with open(path,"a",encoding="utf-8",newline="")as f:
        f_csv=csv.DictWriter(f,headers)
        f_csv.writeheader()
        f_csv.writerows(rows)

def write_csv_headers(path,headers):
    with open(path,"a",encoding="utf-8",newline="")as f:
        f_csv=csv.DictWriter(f,headers)
        f_csv.writeheader()

def write_csv_row(path,headers,row):
    with open(path,"a",encoding="utf-8",newline="")as f:
        f_csv=csv.DictWriter(f,headers)
        f_csv.writerows(row)

def main(url,file_name,headers,pages):

    write_csv_headers(file_name,headers)
    for i in tqdm(range(pages)):
        Articles=[]
        html=get_on_page(url)
        items=parse_one_page(html)
        for item in items:
            Articles.append(item)



        write_csv_row(file_name,headers,Articles)

if __name__=="__main__":
    url = "http://t.10jqka.com.cn/guba/1A0001/"
    file_name = "Article_list" + ".csv"
    headers = ["title"]
    pages=10
    main(url,file_name,headers,1)