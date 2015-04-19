#!/usr/bin/python

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

        cur = conn.cursor()
#        cur.execute('update mysql.user set password = PASSWORD("123123") where user = "root"; flush privileges', multi=True)
#        cur.execute('select user,host,password from mysql.user')
        cur.execute('create table if not exists Tracks (title TEXT, plays INTEGER)')
        cur.execute('INSERT INTO Tracks (title, plays) VALUES ( "Thunderstruck", 20 )')
        cur.execute('INSERT INTO Tracks (title, plays) VALUES ( "My Way", 15 )')
        cur.execute('select * from Tracks')
        for row in cur:
            print(row)

    except Error as error:
        print(error)

    finally:
        conn.commit()
        cur.close()
        conn.close()
        print('Connection closed.')

if __name__ == '__main__':
    connect()
