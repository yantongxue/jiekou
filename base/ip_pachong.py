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
    for title in soup.find_all("div", class_="post-title"):
        title_name=title.string.strip()
        print(title_name)


def get_one_parse(url):
    with open("ip.txt","a+")as f:
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

def validdata(ip):
    IP={"http":ip}
    try:
        r=requests.get("http://www.baidu.com",proxies=IP,timeout=3)#proxies使用指定的代理 IP进行访问
        if r.status_code==200:
            print("成功:{}".format(ip))
            alive_ip.append(ip)
    except:
        print("无效")
def save():
    with open("alive_ip.txt","a+") as f:
        for ip in alive_ip:
            f.write(ip+"\n")
            print(ip)
        print("成功保存所有有效ip")

def  main():
    with open("ip.txt","r") as f:
        lines=f.readlines()
        ips=list(map(lambda x:x.strip(),[line for line in lines]))
        pool=ThreadPool(20)#多线程 设置并发数量
        pool.map(validdata,ips)#用map是简单实现   python程序并行化,第一个参数是函数，第二个是要实现的变量
        save()

if __name__=="__main__":
    main()

