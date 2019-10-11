

import socket


def main():
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    tcp_socket.connect(("10.10.4.16",int(8002)))

    download_file_name=input("请输入要下载文件名字")
    tcp_socket.send(download_file_name.encode("utf-8"))
    recv_data=tcp_socket.recv(1024)


    with open("[xnew]"+download_file_name,"wb") as f:
        f.write(recv_data)


if __name__=="__main__":
    main()
