#!/usr/bin/python

import json
import twurl
import urllib
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

try:
    print('Connecting to MySQL database...')
    db_config = read_db_config()
    conn = MySQLConnection(**db_config)
    if conn.is_connected():
        print('connection established.')
    else:
        print('connection failed.')
    cur = conn.cursor()
#    cur.execute('update mysql.user set password = PASSWORD("123123") where user = "root"; flush privileges', multi=True)
#    cur.execute('select user,host,password from mysql.user')
#    cur.execute('create table if not exists Tracks (title TEXT, plays INTEGER)')
#    cur.execute('''INSERT INTO Tracks (title, plays) VALUES (%s, %s)''', ( "My Way", 15 ) )
#    for row in cur:
#        print(row)
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Twitter
        (name TEXT, retrieved INTEGER, friends INTEGER)
    ''')
    while True:
        acct = raw_input('Enter a Twitter account, or quit: ')
        if ( acct == 'quit' ):
            break
        if ( len(acct) < 1 ):
            cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
            try:
                acct = cur.fetchone()[0]
            except:
                print 'No unretrieved Twitter accounts found'
                continue

        url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'} )

        print 'Retrieving', url
        connection = urllib.urlopen(url)
        data = connection.read()
        headers = connection.info().dict
        # print 'Remaining', headers['x-rate-limit-remaining']
        js = json.loads(data)
        # print json.dumps(js, indent=4)

        cur.execute('''UPDATE Twitter SET retrieved=1 WHERE name = %s''', (acct,) )

        countnew = 0
        countold = 0

        for u in js['users']:
            friend = u['screen_name']
            print friend
            cur.execute('''SELECT friends FROM Twitter WHERE name = %s LIMIT 1''', (friend, ) )
            try:
                count = cur.fetchone()[0]
                cur.execute('''UPDATE Twitter SET friends = %s WHERE name = %s''', (count+1, friend) )
                countold = countold + 1
            except:
                cur.execute('''INSERT INTO Twitter (name, retrieved, friends) VALUES ( %s, 0, 1 )''', ( friend, ) )
                countnew = countnew + 1

        conn.commit()
        print 'New accounts=',countnew,' revisited=',countold

except Error as error:
    print(error)
finally:
    cur.close()
    conn.close()
    print('Connection closed.')
