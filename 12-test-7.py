#!/usr/bin/python3

import urllib
from BeautifulSoup import *

#url = input('Enter - ')
url = "http://www.dr-chuck.com/page1.htm"
url = "http://learnpythonthehardway.org/book/"
url = "http://www.py4inf.com/book.htm"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    print('Tag: %s' % tag)
    print('URL: %s' % tag.get('href', None))
    print('Content: %s' % tag.contents[0])
    print('Attrs: %s' % tag.attrs)
    print('\n')

#print(tags)