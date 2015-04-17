#!/usr/bin/python3

import urllib
import re

#url = input('Enter - ')
url = "http://www.dr-chuck.com/page1.htm"
url = "http://learnpythonthehardway.org/book/"
url = "http://www.py4inf.com/book.htm"
links = list()

fd = urllib.urlopen(url)
for line in fd:
    line = line.strip().lower()
    link = re.findall('href="(http[s]?://\S+?)"', line)
    if len(link) > 0: links += link

for i in links:
    print(i)
