#!/usr/bin/python3

import socket

url = 'http://learnpythonthehardway.org/book/advice.html'
url = 'http://www.py4inf.com/code/romeo.txt'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET %s HTTP/1.0\n\n' % url)

text = str()
while True:
    data = mysock.recv(512)
    if len(data) < 1 : break
    text += data
mysock.close()

body = text[text.find('\r\n\r\n') + 4:]
print(body)
