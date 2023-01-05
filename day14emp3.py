class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("total employee %d" % Employee.empCount)
    def displayEmployee(self):
        print("name:",self.name, ", Salary:",
              self.salary)
emp1=Employee("naina",550000)
emp1.displayEmployee()
print("is salary is an attribute:",hasattr(emp1, 'salary'))
print(getattr(emp1,'salary'))
setattr(emp1,'salary',7000)
print("modified salary",getattr(emp1,'salary'))
print(hasattr(emp1,'desg'))
setattr(emp1,'desg','manager')
print(hasattr(emp1,'desg'))
print("added attribute",getattr(emp1,'desg'))
delattr(emp1,'salary')
print("is salary an attribute:",hasattr(emp1,'salary'))
