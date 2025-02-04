"""
Write a program to calculate the factorial of a given number using a loop.
"""

n = 10
fact = 1

for i in range(1, n + 1):
    if n == 1 or n == 0:
        fact = 1
    fact = fact * i

print(fact)
