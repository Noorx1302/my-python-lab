"""
Write a program to:

Count the number of vowels in a string.

Reverse a string.

Check if a string is a palindrome.
"""

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def rev_str(s):
    return s[::-1]

def is_palindrome(s):
    return s == rev_str(s)



my_str = "This is my string"

print(count_vowels(my_str))
print(rev_str(my_str))
print(f"Is my string palindrome? {is_palindrome(my_str)}")