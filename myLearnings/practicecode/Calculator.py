class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is: {self.num*self.num}")

    def cube(self):
        print(f"The cube of {self.num} is: {self.num*self.num*self.num}")

    def sqaureRoot(self):
        print(f"The square root of {self.num} is: {self.num**0.5}")

c = Calculator(4)
c.square()
c.cube()
c.sqaureRoot()