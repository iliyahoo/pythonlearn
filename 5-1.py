#!/usr/bin/python

count = 0
total = 0
avg = None

while True:
    number = raw_input("Enter a number:\n> ")
    try:
        number = float(number)
    except ValueError:
        if number.lower() == "done": break
        print("It's not numeric. Try again.\n")
    else:
        total += number
        count += 1
        avg = total / count

print(total, count, avg)
