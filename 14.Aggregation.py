class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee


emp = Employee("Sara")
dept = Department("HR", emp)
print(dept.employee.name)
