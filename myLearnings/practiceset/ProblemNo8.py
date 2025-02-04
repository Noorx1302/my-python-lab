"""
Write a program to:

Find the largest number in a list.

Find the sum of all elements in a list.

Remove duplicates from a list.
"""

l = [2, 3, 4, 1, 8, 2]

def is_largest(l):
    return max(l)

def is_sum(l):
    return sum(l)

def remove_duplicates(l):
    return list(set(l))

print(is_largest(l))
print(is_sum(l))
print(remove_duplicates(l))