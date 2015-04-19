#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

#cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE IF NOT EXISTS Tracks (title TEXT, plays INTEGER)')
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

conn.close()