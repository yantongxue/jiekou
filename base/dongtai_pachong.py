from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests
from time import sleep
from multiprocessing.dummy import Pool as ThreadPool
import lxml.html
import random
import pprint





url="http://t.10jqka.com.cn/newcircle/post/getCodePostList/?"
seeds = "1234567890"

random_num = []
#此处是为了生成一个13位的随机数
for i in range(13):

    random_num.append(random.choice(seeds))
random_num="".join(random_num)
page_num=0
for num in range(3):
    page_num=page_num+1

    data = {
        'fid': '2964',
        'type': '0',
        'page': page_num,
        '_': random_num,

}

#下面的session  以及params是为了将get请求可以以data的形式
    s  = requests.session()
    res=s.get(url, params = data).json()
    html=res["result"]["html"]

    soup=BeautifulSoup(html,"html.parser")
    for title in soup.find_all("div",class_="post-title"):
        if title.string==None:
            print(title.string)
        else:
            print(title.string.strip())