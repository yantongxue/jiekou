import logging


#logging.basicConfig(level=logging.DEBUG,
                    #filename="./log.txt",
                    #filemode="a",
                    #format="%s(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s")

#logging.debug("测试哈哈哈哈哈哈哈")


class Test:
    a=10

    def xiugaui(self):


        print("局部变量是")

    print("全局变量是%s"%a)
b=Test().xiugaui()
b1=Test().xiugaui()


