import socket
from time import sleep
import re

def  service_client(new_socket,request):



    request_lines=request.splitlines()

    ret=re.match(r"[^/]+(/[^ ]*)",request_lines[0])

    file_name=""
    if ret:
        file_name=ret.group(1)

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
        response_body=html_content

        response_header = "HTTP/1.1 200 OK\r\n"

        response_header+="Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response=response_header.encode("utf-8")+response_body
        new_socket.send(response)

        new_socket.send(html_content)





def main():
    tcp_service_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_service_socket.bind(("",int(8009)))
    tcp_service_socket.listen(128)
    tcp_service_socket.setblocking(False)#设置套接字为非堵塞的方式

    new_socket_list=list()
    while True:

        try:
            new_socket,new_add=tcp_service_socket.accept()


        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            new_socket_list.append(new_socket)



        for new_socket in new_socket_list:
            try:
                recv_data=new_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_data:
                    service_client(new_socket,recv_data)
                else:
                    new_socket.close()
                    new_socket_list.remove(new_socket)
                    print("客户端关闭了")




if __name__=="__main__":
    main()