#!/usr/bin/python3

import urllib

#url = input('Enter web address: ')
#if len(url) == 0:
#    url = 'http://www.py4inf.com/code/romeo.txt'
url = 'http://www.py4inf.com/code/romeo.txt'
url = 'http://learnpythonthehardway.org/book/advice.html'

domain = url.split('/')[2]
proto = url.split('/')[0].rstrip(':')

try:
    port = domain.split(':')[1]
except IndexError:
    if proto == 'http': port = 80
    elif proto == 'https': port = 443

ud = urllib.urlopen(url)

size = 0
while True:
    text = ud.read(3000)
    if len(text) < 1: break
    size += len(text)
#    if size <= 3000 : print(text)
    print(text)

print('%s characters' % size)
