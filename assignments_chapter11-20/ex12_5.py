import socket
import re

name = input('Enter a hostname : ')
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = name.split('/')
try:
    mysock.connect((url[2], 80))
except:
    print('Error, can\'t connect to the host')
    quit()

#cmd = ('GET http://' + name +  ' HTTP/1.0\r\n\r\n').encode()
cmd = ('GET %s HTTP/1.0\r\n\r\n' % name).encode()
mysock.send(cmd)

doc = ''
while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    doc += data.decode()
    #print(data.decode(), end = '')
pos = doc.find('\r\n\r\n')
print(doc[pos + 4:])
