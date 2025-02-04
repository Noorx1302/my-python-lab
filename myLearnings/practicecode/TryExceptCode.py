def division(n):
    try:
        div = 10 / n
    except ArithmeticError as e:
        print(e)
    finally:
        print("Finally")


division(0)