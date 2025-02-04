def convertFahrenheit(celsius):
    temp = (celsius * (9 / 5)) + 32
    return temp


print(f"{convertFahrenheit(38)}, converted to Fahrenheit", end="")
print(" in same line")
