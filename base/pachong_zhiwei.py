import requests
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

url="http://t.10jqka.com.cn/api.php?method=trace.getListByFids&fids=14874%2C19470%2C20010%2C3293%2C91310%2C46080%2C47399&id=0&limit=10&renderCount=1&sort=down"
res=requests.get(url).json()

l=len(res["result"]["html"])
title_list=[]
content_list=[]
#for i  in range(l):

    #title_list.append(res["result"]["html"][i]["title"])
    #content_list.append(res["result"]["html"][i]["content"])

#words_df=pd.DataFrame({"title":title_list,"content":content_list})
#words_df.to_csv("title_content.csv",encoding="gbk")

df=pd.read_csv("title_content.csv",encoding="gbk")

df.drop(df[df['职位名称'].str.contains('实习')].index, inplace=True)#.index就是这满身包括“实习”的这一行的索引,注意：凡是会对原数组作出修改并返回一个新数组的，往往都有一个 inplace可选参数。如果手动设定为True（默认为False），那么原数组直接就被替换。也就是说，采用inplace=True之后，原数组名（如2和3情况所示）对应的内存值直接改变；

pattern="\d+"#此处的\d 代表[0-9},+匹配前一个数字一次或者多次
#print(df["工作经验"])

df["工作年限"]=df["工作经验"].str.findall(pattern)#将字符串转化为列表
avg_work_year=[]
for i  in  df["工作年限"]:
    if len(i)==0:
        avg_work_year.append(0)
    elif len(i)==1:
        avg_work_year.append(int("".join(i)))#此处如果直接用int(i）是因为i是list不可以直接转换为int,所以经过"".join(i) 将i变为了str类型
    else:
        num_list=[int(j) for j in i]
        avg_year=sum(num_list)/2
        avg_work_year.append(avg_year)
#print(avg_work_year)
df['salary'] = df['工资'].str.findall(pattern)

avg_salary = []
for k in df['salary']:
   int_list = [int(n) for n in k]
   avg_wage = int_list[0]+(int_list[1]-int_list[0])/4
   avg_salary.append(avg_wage)

df['月工资'] = avg_salary
df["经验"]=avg_work_year


df.to_csv("title_content.csv",index=False,encoding="gbk")#此处的保存可以将上面的一系列操作比如drop的操作都进行了保存


mpl.rcParams['font.sans-serif'] = ['SimHei']#指定字体，如果不写这个的h话，直方图中的汉字不显示
#print('数据分析师工资描述：\n{}'.format(df['月工资'].describe()))#describe参考链接：https://www.cnblogs.com/batteryhp/p/5006274.html，就是整体描述，比如平均值等
plt.hist(df["月工资"],bins=12)
plt.xlabel("工资 (千元)")
plt.ylabel("频数")
plt.title("工资直方图")
plt.savefig("title_content.png")
plt.show()


