#!/usr/bin/python3

word = input('Enter word :\n> ')
letter = input('Enter letter :\n> ')

def count(word, letter):
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count

result = count(word, letter)
print(result)
