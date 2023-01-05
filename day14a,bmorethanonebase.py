class A:
    def first_method(self):
        print("method of class A....")
class B:
    def second_method(self):
        print("method of class B....")
class C(B,A):#B,A
    def third_method(self):
        print("method of class C....")
        #super().first_method()
if __name__=='__main__':
    ob=C()
    ob.first_method()
    #ob.second_method()
    ob.third_method()
    #c().third_method()
#circular inheritance is not possible
    
