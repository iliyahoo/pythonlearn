#!/usr/bin/python3

import xml.etree.ElementTree as ET
import json

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Phone: ', tree.find('phone').text.strip())
print('Attr: ', tree.find('email').get('hide'))

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count: ', len(lst))

for item in lst:
    print('Name: ', item.find('name').text)
    print('ID: ', item.find('id').text)
    print('Attribute: ', item.get('x'))

input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]
'''
info = json.loads(input)
print(info)
exit()
print('User count: ', len(info))
for user in info:
    print('Name: ', user['name'])
    print('Id: ', user['id'])
    print('Attr: ', user['x'])
