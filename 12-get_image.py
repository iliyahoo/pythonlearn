#!/usr/bin/python3

import socket
import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')

count = 0
pic = str()
while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    # time.sleep(0.25)
    count += len(data)
    print(len(data), count)
    pic += data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = pic.find('\r\n\r\n')
print('Header length: ', pos)
print('')
print(pic[:pos])
print('')

# Skip past the header and save the picture data
pic = pic[pos+4:]
fd = open('cover.jpg', 'wb')
fd.write(pic)
fd.close()
