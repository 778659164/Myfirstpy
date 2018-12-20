import socket
client =socket.socket()
client.connect(('127.0.0.1',6971))
while True:
    data=input('输入要发送的数据>>>')
    if data=='q':
        print('下线')
        client.close()
    client.send(data.encode())
    rec_data=client.recv(1024)
    print('接收的数据是：%s'% rec_data.decode('utf-8'))