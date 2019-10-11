
import multiprocessing

def downlown_data(q):

    data=[1,"hahhas",66666,"hshsbcbbdbbv",9999999]
    for temp in data:
        q.put(temp)
    print("下载器已经下载完了数据保存在了队列中.........")

def anaylsy_data(q):
    waiting_data=list()

    while True:
        get_data=q.get()
        waiting_data.append(get_data)
        if q.empty():
            break


    print(waiting_data)



def main():
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=downlown_data,args=(q,))
    p2=multiprocessing.Process(target=anaylsy_data,args=(q,))
    p1.start()
    p2.start()



if  __name__=="__main__":
    main()