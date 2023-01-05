class vector2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,ob):
        return vector2d(self.x+ob.x,self.y+ob.y)
    def __sub__(self,other):
        return vector2d(self.x-other.x,self.y-other.y)
first=vector2d(5,8)
second=vector2d(3,7)
result=first+second
print(result.x)
print(result.y)
result=first-second
print(result.x)
print(result.y)
"""__mul__'  __tuediv__,__floordiv__//__mod__%,__pow__**__and__&__xor__^__or__|"""
