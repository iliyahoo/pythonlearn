#!/usr/bin/python3

import urllib
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

acct = 'fixpert'
acct = 'ILIyahoo'
if len(acct) < 1 :
    exit()
url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'} )
print 'Retrieving', url
connection = urllib.urlopen(url)
data = connection.read()
headers = connection.info().dict
print 'Remaining', headers['x-rate-limit-remaining']
js = json.loads(data)
print json.dumps(js, indent=4)
for u in js['users'] :
    print u['screen_name']
    s = u['status']['text']
    print ' ',s[:50]
