"""
def rev_string(myStr):
    rev_str = ""
    for char in myStr:
        rev_str = char + rev_str
    return rev_str


myStr = "Hello, Good Morning everyone"
print(rev_string(myStr))


def rev_list(myList):
    rev_l = []
    for i in myList:
        rev_l.insert(0, i)
    return rev_l


myList = [1, 2, 3, "Me"]
print(rev_list(myList))


def rev_str(s):
    rev_string = ""
    for char in s:
        if char == " " or char == "o":
            rev_string = "66" + rev_string
        rev_string = char + rev_string
    return rev_string


s = "Hello world, welocme to the python"
print(rev_str(s))


try:
    a = 10/0
except ZeroDivisionError as e:
    print("messed up")


"""
import decimal
int_num = 10
dec_num = decimal.Decimal(int_num)
print(dec_num)
print(type(dec_num))

import decimal
s = "12345"
dec_con = decimal.Decimal(s)
print(dec_con)
print(type(dec_con))

s = "MyNameIsKhan"
slc_s = s[::-1]
print(slc_s)


s = "suckers so the best"
def count_vowels(s):
    vow = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vow:
            count += 1
    return count

print(count_vowels(s))


s = "abcdefghi"

def count_consonants(s):
    vow = "aeiouAEIOU"
    count = 0
    for char in s:
        if char not in vow:
            count += 1
    return count

print(count_consonants(s))

s = "abcadeafghi"

def count_a(s):
    a = "a"
    count = 0
    for i in s:
        if i == a:
            count += 1
    return count

print(count_a(s))


# 0, 1, 1, 2, 3, 5
def fibonacci(n):
    my_list = []
    for i in range(n + 1):
        if i == 0:
            my_list.append(0)
        elif i == 1:
            my_list.append(1)
        else:
            fib_ser = my_list[i - 1] + my_list[i - 2]
            my_list.append(fib_ser)
    return my_list


n = 10
print(fibonacci(n))


def max_list(l):
    max_num = l[0]
    for num in l:
        if num > max_num:
            max_num = num
    return max_num

l = [10, 50, 9, 100, 1]
print(max_list(l))


def min_list(l):
    min_num = l[0]
    for num in l:
        if num < min_num:
            min_num = num
    return min_num

l = [10, 50, 9, 100, 1]
print(min_list(l))


def middle_num(l):
    mid_num = int(len(l) / 2)
    return l[mid_num]

l = [10, 50, 9, 100, 1]
print(middle_num(l))


def str_conv(l):
    s = ""
    for char in l:
        s = s + str(char)
    return s

l = [10, 50, 9, 100, 1, "Noor"]
print(str_conv(l))


def add_lists(l1, l2):
    l3 = []
    for i in range(0, len(l2)):
        l3.append(l1[i] + l2[i])
    return l3


l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(add_lists(l1, l2))



def is_anagram(str1, str2):
    str1 = list(str1.lower())
    str2 = list(str2.lower())
    str1.sort()
    str2.sort()

    if str1 == str2:
        return "sorted"
    else:
        return "not sorted"


str1 = "Worth"
str2 = "thRow"
print(is_anagram(str1, str2))



def is_palindrome(s):
    if s.lower() == s[::-1].lower():
        return "palindrome"
    return "Not palindrome"

s = "Gadag"
print(is_palindrome(s))



