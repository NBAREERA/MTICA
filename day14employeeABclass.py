class A:
    pass
class B:
    pass
class employee(A,B):
    """derived class employee inherits from base class A and B"""
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empCount+=1
    def displayCount(self):
        print("total employee %d"% employee.empCount)
    def displayemployee(self):
        print('name:",self
