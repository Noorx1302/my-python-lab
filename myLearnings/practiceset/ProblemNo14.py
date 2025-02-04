def second_largest(l):
    max_list = max(l)
    l.remove(max_list)
    second_larg = max(l)
    return second_larg

l = [33, 44, 55, 11, 22]
print(second_largest(l))