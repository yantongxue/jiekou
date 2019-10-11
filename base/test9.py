#coding=utf-8
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests
from time import sleep
from multiprocessing.dummy import Pool as ThreadPool
import lxml.html
import re
import pandas as pd
import csv

file = open('D:/jiekou2/base/view-source_www.dianping.com_hangzhou_ch10_g110.html', 'r', encoding='utf-8')

soup = BeautifulSoup(file, 'lxml')
address_list=[]
for i in soup.find_all("div", "tag-addr"):
    address = i.a.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string
    address_list.append(address)

data={
    "address":address_list
}

address_data=pd.DataFrame(data=data)
address_data.to_csv("data.csv")