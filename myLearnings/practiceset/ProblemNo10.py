"""
Write a program that prints numbers from 1 to 100. For multiples of 3,
print "Fizz" instead of the number. For multiples of 5, print "Buzz".
For numbers that are multiples of both 3 and 5, print "FizzBuzz".
"""


def fizzBuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


print(fizzBuzz())