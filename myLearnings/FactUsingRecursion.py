n = 3

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

print(f"This is my factorial: {fact(n)}")