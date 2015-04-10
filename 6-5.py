#!/usr/bin/python3

str = 'X-DSPAM-Confidence: 0.8475'

startpos = str.find(':')
num = float(str[startpos + 1:])
print(num)
