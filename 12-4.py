#!/usr/bin/python3

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = 'http://learnpythonthehardway.org/book/advice.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the paragraph tags
tags = soup('p')
print(len(tags))
