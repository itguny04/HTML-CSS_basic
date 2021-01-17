from socket import *

sock = socket(AF_INET,SOCK_STREAM)
sock.connect(('127.0.0.1',10000))

print('연결됨.')

while True:
    data = sock.recv(1024)
    print('>', data.decode('utf-8'))

    msg = input('> ')
    if msg == ':q!':
        sock.send(msg.encode('utf-8')) 
        sock.close() 
        break

    sock.send(msg.encode('utf-8')) 