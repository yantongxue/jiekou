from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests
from time import sleep
from multiprocessing.dummy import Pool as ThreadPool
import lxml.html
import re
import pandas as pd










def  main():
    for i  in range(1,3):
        url="http://www.dianping.com/search/keyword/3/0_%E5%B0%8F%E9%BE%99%E8%99%BE/p{}"
        #url=url.format(i)
        #html=get_on_page(url)





if __name__=="__main__":

    file = open('D:/jiekou2/base/view-source_www.dianping.com_hangzhou_ch10_g110.html', 'r', encoding='utf-8')
    #print(file)
    soup = BeautifulSoup(file, 'lxml')

    title_list=[]
    url_list=[]
    xingji_list=[]
    review_num_list=[]
    mean_prince_list=[]
    address_list=[]
    for i   in  soup.find_all("div",class_="tit"):
        title=i.a.h4.string#注意此处找到一个a标签，然后在继续在a标签下面找h4标签
        url=i.a.get("href")
        title_list.append(title)
        url_list.append(url)

    for i in soup.find_all("div", class_="comment"):
        xingji = i.span.get("title")  # 注意此处找到一个a标签，然后在继续在a标签下面找h4标签
        review_num= i.a.b.string
        mean_prince=i.a.next_sibling.next_sibling.next_sibling.next_sibling.b.string
        xingji_list.append(xingji)
        review_num_list.append(review_num)
        mean_prince_list.append(mean_prince)



    for i in soup.find_all("div","tag-addr"):
        address=i.a.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string
        address_list.append(address)

    data={
        "title(店铺名称）":title_list,
        "url":url_list,
        "xingji（星级）":xingji_list,
        "review_num（评论数量）":review_num_list,
        "mean_prince(人均）":mean_prince_list

    }
    dazhong_data=pd.DataFrame(data=data)
    dazhong_data.to_csv("dazhong.csv",encoding="gbk")