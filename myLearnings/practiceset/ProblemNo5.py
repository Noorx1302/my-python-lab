"""
Write a program to generate the first n numbers of the Fibonacci sequence.
"""

def fibonacci(n):
    sequence = []
    num1, num2 = 0,1
    for i in range(1, n+1):
        sequence.append(num1)
        num1, num2 = num2, num1+num2
    return sequence

print(fibonacci(10))
