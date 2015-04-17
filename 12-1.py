#!/usr/bin/python3

import socket

#url = input('Enter web address: ')
#if len(url) == 0:
#    url = 'http://www.py4inf.com/code/romeo.txt'
url = 'http://learnpythonthehardway.org/book/advice.html'

domain = url.split('/')[2]
proto = url.split('/')[0].rstrip(':')

try:
    port = domain.split(':')[1]
except IndexError:
    if proto == 'http': port = 80
    elif proto == 'https': port = 443

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((domain, port))
except:
    print('URL %s is wrong' % url)
    exit()

mysock.send('GET %s HTTP/1.0\n\n' % url)

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print(data)

mysock.close()
