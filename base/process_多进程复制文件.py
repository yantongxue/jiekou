import os
import multiprocessing
from multiprocessing import managers

def copy_file(q,file_name,old_folder_name,new_folder_name):
    old_f=open(old_folder_name+"/"+file_name,"rb")
    content=old_f.read()
    #print(content)
    #print(content.decode("gbk"))
    old_f.close()

    new_f=open(new_folder_name+"/"+file_name,"wb")
    new_f.write(content)
    new_f.close()
    q.put(file_name)


def main():

    #1.输入要拷贝的文件夹的
    old_folder_name=input("请输入要拷贝的文件夹名称：")
    new_folder_name=None
    #2.创建一个新的文件夹
    try:
        new_folder_name=old_folder_name+"[复件]"
        os.mkdir(new_folder_name)
    except:
        pass


    #3 获得文件夹中的所有文件
    files_name=os.listdir(old_folder_name)
    #print(files_name)


    #创建多进程复制文件
    po=multiprocessing.Pool(5)
    #创将一个队列
    q=multiprocessing.Manager().Queue()

    #向进程池中添加要复制的文件
    for file_name in files_name:
        po.apply_async(copy_file,args=(q,file_name,old_folder_name,new_folder_name))

    po.close()

    all_need_file=len(files_name)
    copy_ok_num=0
    while True:
        file_name=q.get()
        print("已经完成%s"%file_name)
        copy_ok_num+=1

        print("复制的进度是%.2f %%"%(copy_ok_num*100/all_need_file))
        if copy_ok_num>=all_need_file:
            break

if __name__ =="__main__":
    main()