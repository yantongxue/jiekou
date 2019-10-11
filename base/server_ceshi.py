import socket


def main():
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.bind(("",8002))
    tcp_server_socket.listen()
    print("111111")
    while True:
        new_client_socket,client_addrr=tcp_server_socket.accept()
        print("222222")
        file_name=new_client_socket.recv(1024).decode("utf-8")

        print("客户端（%s）需要下载的文件是：%s"%(str(client_addrr),file_name))


        new_client_socket.send("hahahahhahah".encode("utf-8"))

        new_client_socket.close()
    tcp_server_socket.close()


if __name__=="__main__":
    main()