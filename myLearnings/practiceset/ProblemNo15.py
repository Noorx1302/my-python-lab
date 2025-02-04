"""
Write a program to print the multiplication table of a given number.
"""


def mult_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


mult_table(20)