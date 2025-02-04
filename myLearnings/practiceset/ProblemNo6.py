"""
Write a program to check if a given string is a palindrome (reads the same backward as forward, e.g., "madam")
"""

def isPalindrome(myStr):
    if myStr.lower() == myStr[::-1].lower():
        print("Palindrome")
    else:
        print("Not Palindrome")

isPalindrome("Gadag")