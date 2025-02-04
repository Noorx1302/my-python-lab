"""
Write a program that checks if a given number is even or odd.
"""

num = 100

if num == 0:
    result = "Num is 0"
elif num % 2 == 1 or num == 1:
    result = "Is an odd number"
else :
    result = "Is an even number"

print(result)