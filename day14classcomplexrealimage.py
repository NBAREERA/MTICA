class complex:
    def __init__(self,real,image):
        self.real=real
        self.image=image
    def __mul__(self,ob):
        temp=(self.real*ob.real-self.image*ob.image,self.real*ob.image+self.image
              *ob.real)
        return temp
    def __str__(self):
        return(self.real,self.image)
ob1=complex(3,5)
ob2=complex(5,7)
ob3=ob1*ob2
print(ob3)

