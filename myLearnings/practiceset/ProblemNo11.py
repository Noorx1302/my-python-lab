"""
Write a program that takes a sentence as input and counts the number of words in it.
"""

def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Enter a sentence: ")

print(count_words(sentence))