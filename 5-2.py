#!/usr/bin/python

minimal = None
maximal = None

while True:
    number = raw_input("Enter a number:\n> ")
    try:
        number = float(number)
    except ValueError:
        if number.lower() == "done": break
        print("It's not numeric. Try again.\n")
    else:
        if minimal is None or maximal is None:
            minimal = maximal = number
        elif number < minimal:
            minimal = number
        elif number > maximal:
            maximal = number

print(minimal, maximal)
