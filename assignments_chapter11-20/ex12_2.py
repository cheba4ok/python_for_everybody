import socket

name = input('Enter a hostname : ')
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = name.split('/')
try:
    mysock.connect((url[0], 80))
except:
    print('Error, can\'t connect to the host')
    quit()

#cmd = ('GET http://' + name +  ' HTTP/1.0\r\n\r\n').encode()
cmd = ('GET http://%s HTTP/1.0\r\n\r\n' % name).encode()
mysock.send(cmd)

number = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    for entry in data:
        number += 1
    if number > 3000 : break
    print(data.decode(), end = '')
    #print('test')
print ('Number of symbols : ', number)
mysock.close()
