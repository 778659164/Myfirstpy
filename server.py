import socket
server =socket.socket()
server.bind(('',6971))
server.listen(5)#排队的长度
print('等待链接')
conn, addr=server.accept()    #阻塞
while True:
    print('等待接收')
    data=conn.recv(1024)
    print(data.decode('utf-8'))
    if data:
        conn.send(data)
    else:
        conn.close()
        break

