class Programmer:
    def __init__(self, name, empId):
        self.name = name
        self.empId = empId
        # print(f"Name and empId of this employee is {name} and {empId}")


emp1 = Programmer("Noor", 141)

print(emp1.name, emp1.empId)