class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("total employee {0}".format(Employee.empCount))
    def displayEmployee(self):
        print("name:",self.name, ", Salary:",
              self.salary)
emp1=Employee("naina",550000)
emp1.displayEmployee()
emp1.salary=17000
emp1.experience=3
emp1.displayEmployee()
emp1.name='moto'
emp1.displayEmployee()
print(emp1.experience)
#del emp1.salary
emp1.displayEmployee()

