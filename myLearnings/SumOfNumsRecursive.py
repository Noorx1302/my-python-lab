def sumOfNumsRecursive(n):
    if n == 0:
        return 0
    return n + sumOfNumsRecursive(n - 1)

print(sumOfNumsRecursive(4))