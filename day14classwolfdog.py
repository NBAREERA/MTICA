class wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("grrr....")
        
class dog(wolf):
    def bark(self):
        print("woohuwooohu.....")
pet1=dog("tommy","brown")

pet1.bark()
pet2=wolf("jimmy","grey")
pet2.bark()
dog("abc","xyz").bark()
