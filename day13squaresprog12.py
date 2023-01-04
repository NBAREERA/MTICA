def squares(x=0):
    while x<11:
        x=x+1
        yield x*x
##yieldList=[i for i in squares()]
##print(yieldList)

#Materialise list from generator using list()
yieldList=list(squares())
print(yieldList)
