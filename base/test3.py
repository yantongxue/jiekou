from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests
from time import sleep
from multiprocessing.dummy import Pool as ThreadPool
import lxml.html

alive_ip=[]
def get_on_page(url):

    try:
        response = requests.get(url)
        if response.status_code==200:
            return (response.text)
        return  None
    except RequestException as e:
        return None


def get_data(html):
    soup=BeautifulSoup(html,"html.parser")


    for title in soup.find_all("a", ):
        title_name=title.string.strip()
        print(title_name)


def get_one_parse(url):
    with open("XiaoLongXia.txt","a+")as f:
        print(url)
        html=get_on_page(url)
        html=lxml.html.etree.HTML(html)#解析下载的数据html
        IP=html.xpath('//*[@id="list"]/table/tbody//td[1]/text()')#获取元素的Xpath信息  file=s.xpath('元素的xpath信息/text()'
        #print(IP)
        poots=html.xpath('//*[@id="list"]/table/tbody//td[2]/text()')
        #print(poots)
        for (ip,poot) in zip(IP,poots):#zip就是讲2个list打包为元组，
            ip=ip+":"+poot
            #print("测试:{}".format(ip))
            f.write(ip+'\n')



def  main(url):
    for i  in range(10):
        html=get_on_page(url)
        data=get_data(html)




if __name__=="__main__":
    main()