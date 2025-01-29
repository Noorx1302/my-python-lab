def greatestNum(num1,num2, num3):
    if num1>num2 and num1>num3:
        return num1
    elif(num1<num2 and num2>num3):
        return num2
    else:
        return num3

print(f"The greatest number is {greatestNum(10,2,3)}")