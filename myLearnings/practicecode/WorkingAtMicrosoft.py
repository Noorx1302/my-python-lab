class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

emp1 = Programmer("King", 20000, "QA")
print(emp1.name, emp1.salary, emp1.designation)
