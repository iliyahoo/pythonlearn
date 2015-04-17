#!/usr/bin/python3

import urllib

count = dict()

fd = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fd:
    line = line.strip().lower()
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

print(count)

