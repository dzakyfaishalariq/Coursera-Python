import socket

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #atau \n\n
data.send(cmd)
while True:
    data1 = data.recv(512)
    if(len(data1) < 1):
        break
    print(data1.decode())
data.close()