"""Write a program that takes two numbers and an operator (+, -, *, /)
 as input and performs the corresponding arithmetic operation."""

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
myOperator = input("Enter your operator: ")

if(myOperator == "+"):
    result = num1+num2
elif(myOperator == "-"):
    result = num1+num2
elif(myOperator == "*"):
    result = num1*num2
else:
    result = num1/num2

print(result)