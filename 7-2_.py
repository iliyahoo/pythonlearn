#!/usr/bin/python3

# Use the file name mbox-short.txt as the file name
#fname = raw_input("Enter file name: ")
fname = "/home/iliya/repositories/PythonLearn/code/mbox-short.txt"
fh = open(fname)

x = 0
num = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x += 1
    num += float( line.split()[1] )
print(num / x)
