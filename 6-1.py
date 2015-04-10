#!/usr/bin/python

string = "Hello, world!"

for index in range(1, (len(string) + 1)):
    print(string[-index])

print(string[::-1])
