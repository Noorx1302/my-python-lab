"""
Write a program to check if a given number is a prime number.
"""


def is_prime(num):
    if num <= 1:
        return f"{num} is not a prime num"
    for i in range(2, num + 1):
        if num % i == 0:
            return f"{num} is a prime num"
    return f"{num} is not a prime num"


i = 1
while i <= 5:
    num = int(input("Enter a number: "))
    print(is_prime(num))
    i = i + 1