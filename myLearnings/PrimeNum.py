myNum = 1

for i in range(2, myNum):
    if (myNum % i) == 0:
        print("Is not prime num")
        break
else:
    print("Is prime num")