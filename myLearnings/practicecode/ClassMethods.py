class Demo:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    def instance_method(self):
        print("instance method")
    @classmethod
    def class_method(cls):
        print("class method")
    @staticmethod
    def static_method():
        print("static method")

a = Demo("name", "num")
a.instance_method()

Demo.class_method()
Demo.static_method()