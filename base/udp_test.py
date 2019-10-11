import socket
import threading

def recv(udp_socket):
    while True:
        recv_data=udp_socket.recvfrom(1024)
        print(recv_data)

def send(udp_socket):
    while True:
        send_data = input("请输入要发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"), ("127.0.0.1", int(8005)))


def main():
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    udp_socket.bind(("",8003))



    t_recv=threading.Thread(target=recv,args=(udp_socket,))
    t_send = threading.Thread(target=send, args=(udp_socket,))

    t_recv.start()

    t_send.start()



if  __name__=="__main__":
    main()