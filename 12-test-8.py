#!/usr/bin/python3

import urllib

url = "http://www.py4inf.com/cover.jpg"
uh = urllib.urlopen(url)
fh = open('cover.jpg', 'w')

size = 0
while True:
    info = uh.read(100000)
    if len(info) < 1: break
    size += len(info)
    fh.write(info)

fh.close()
print('%s characters copied' % size)