"""
Write a program to check if a given number is a prime number.
"""

def is_prime(num):
    if num == 2:
        print("Is a prime num")
    for i in range (2, num):
        if num%i == 0:
            print("Is not a prime num")
            break
        else:
            print("Is a prime num")
            break

is_prime(7)