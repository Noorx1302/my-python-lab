a = int(input("Num1: "))
b = int(input("Num2: "))
c = int(input("Num3: "))
d = int(input("Num4: "))

if(a > b and a > c and a > d):
    print("Num1 is the greatest number")
elif(b > a and b > c and b > d):
    print("Num2 is the greatest number")
elif (c > a and c > b and c > d):
    print("Num3 is the greatest number")
else :
    print("Num4 is the greatest number")