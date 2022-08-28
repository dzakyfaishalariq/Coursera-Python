# mempelajari HTTP untuk mengconekan ke python
"""
    nama : Dzaky Faishalariq
    Mahasisw
"""
import socket
# http://data.pr4e.org/romeo.txt
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #atau \n\n
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()
