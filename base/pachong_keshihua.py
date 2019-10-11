import jieba
import pandas as pd
import numpy
from wordcloud import WordCloud,ImageColorGenerator
from scipy.misc import imread
import matplotlib.pyplot as plt

def  write_txt_file(path,txt):
    with open(path,"a",encoding="utf-8",newline="")as f:

        f.write(txt)

def read_txt_file(path):
    with open(path,"r",encoding="utf-8",newline="")as f:
        return f.read()


if __name__=="__main__":
    txt_filename="ceshi.txt"
    text="必须有强烈的好奇心、很强的逻辑思维能力、吃苦耐劳的精神、擅长模仿、勇于创新负责组织有关部门编定中长期科研计划、新产品发展计划根据新产品开发计划组织领导各项新产品的研究与设计工作，工装工艺设计及工艺管理工作，做到分工合理，全面完成公司下达的各项计划向分管经理建议新产品的试验鉴定；参与验收，并负责组织评定推荐新产品成果上报工作认真贯彻国家的技术政策，保证新产品的技术水平，提高公司经济效益开展对新产品开发和引进技术的测试及试验研究工作广泛收集各类信息（新材料、工艺、产品、设备、新产品市场信息、各类会议、会展、洽谈会信息,组织会议等"
    #write_txt_file(txt_filename,text)
    content=read_txt_file(txt_filename)
    segment=jieba.lcut(content)
    words_df=pd.DataFrame({"segment":segment})
    stopwords=pd.read_csv("chineseStopWords.txt",index_col=False,quoting=3,sep=" ",names=["stopword"],encoding="gbk")#注意此处的quoting是对于一些有2个双引号，一般只会显示一个，增加quoting只会可以显示全
    words_df=words_df[~words_df.segment.isin(stopwords.stopword)]#这里words_df.segment中的segemet是索引的意思，也就是找到这一列，stopwords.stopword与他的意思相同，isin就是不包含的意思
    #print(words_df)
    words_stat=words_df.groupby(by=["segment"])["segment"].agg({"计数":numpy.size})#agg计数可以参考链接https://segmentfault.com/a/1190000012394176
    words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)#sort_values降序的意思，reset_index对索引进行正常排序，ascending=False也就是降序的意思

    color_mask=imread("1.png")#打开背景图片哦
    wordcloud=WordCloud(font_path="simhei.ttf",#设置字体可以显示中文，字体是黑体
                        background_color="white",#背景颜色哦
                        max_words=100,#词云显示的最大词数
                        mask=color_mask,#设置北京图片
                        max_font_size=100,#字体最大值
                        random_state=42,
                        width=1000,height=860,margin=2)


    word_frequence={x[0]:x[1] for x in words_stat.head(100).values}#.head就是获取前面的100个
    #print(word_frequence)
    #word_frequence_dict={}
    #for key in  word_frequence:
        #word_frequence_dict[key]= word_frequence[key]
    #print(word_frequence_dict)
    #print(type(word_frequence_dict))
    wordcloud.generate_from_frequencies(word_frequence)#这一步就是为了绘制词云
    image_colors=ImageColorGenerator(color_mask)#这个和下面的这一句是为了设置词语的颜色和之前整个背景图片的颜色一致
    wordcloud.recolor(color_func=image_colors)
    wordcloud.to_file(("output.png"))#保存生成的词云图片




