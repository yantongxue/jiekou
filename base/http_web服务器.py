import socket
import re
import gevent
from gevent import monkey
import multiprocessing
from  base import mini_frame
class Server():

    def __init__(self):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.tcp_server_socket.bind(("", 8002))
        self.tcp_server_socket.listen(128)

    def  service_client(self,new_socket):
        request=new_socket.recv(1024).decode("utf-8")


        request_lines=request.splitlines()
        print(request_lines)

        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        file_name=""

        if ret:
            file_name=ret.group(1)


        if not file_name.endswith(".py"):

            try:
                f = open("./html" + file_name, "rb")
            except:
                response="HTTP/1.1 502 NOT FOUND\r\n"
                response+="\r\n"
                response+="_______file not found_____"
                new_socket.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()

                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"

                new_socket.send(response.encode("utf-8"))

                new_socket.send(html_content)
        else:
                #如果是以.py结尾,那么认为是动态资源的请求


            header = "HTTP/1.1 502 NOT FOUND\r\n"
            header += "\r\n"

            body=mini_frame.application(file_name)
            response=header+body
            new_socket.send(response.encode("utf-8"))

        new_socket.close()

    def run_forever(self):

        while True:

            new_socket,client_addrr=self.tcp_server_socket.accept()

            p=multiprocessing.Process(target=self.service_client,args=(new_socket,))
            p.start()

            new_socket.close()



    def __del__(self):
        self.tcp_server_socket.close()

def main():
    new_server=Server()
    new_server.run_forever()




if __name__=="__main__":
    main()