def PrintAdd(a,b):
    return a+b
def PrintSub(a,b):
    return a-b
def PrintMul(a,b):
   return a*b
def PrintDiv(a,b):
    return a/b
def choice():
    print("+:Addition");print("-:Substraction");print("*:Multiplication");
    print("/:Division"); print("q:Quit")
    return
colorselect={"+":PrintAdd,"-": PrintSub,"*":PrintMul,"/":PrintDiv}
while True:
    choice()
    selection=input("select arithemetic operation:")
    if selection=='q' or selection=='Q':break
    if ((selection=='+') or(selection=='-')or
    (selection=='*') or (selection=='/')):
          n1=int(input("enter first no:"))
          n2=int(input("enter second no:"))
          z=colorselect[selection](n1,n2)
          print(n1,selection,n2,'=',z)
