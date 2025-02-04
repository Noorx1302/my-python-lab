"""
Write a program where the user has to guess a randomly generated number between 1 and 100.
Provide hints like "Too high" or "Too low" until they guess the correct number.
"""

from random import randint

randNum = randint(1,101)

while True:
    n = int(input("Enter your num: "))
    if n > randNum:
        print("You entered higher number")
    elif n < randNum:
        print("You entered smaller number")
    else:
        print(f"Correct guess {n}")
        break

