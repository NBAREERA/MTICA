def printMonth(dn):
    mn=' '
    if(dn==1):
        return'january'
    elif(dn==2):
        mn='february'
    elif(dn==3):
        mn='march'
    elif(dn==4):
        mn='april'
    elif(dn==5):
        mn='may'
    elif(dn==6):
        mn='june'
    elif(dn==7):
        mn='july'
    elif(dn==8):
         mn='august'
    elif(dn==9):
        mn='september'
    elif(dn==10):
        mn='october'
    elif(dn==11):
        mn='november'
    elif(dn==12):
        mn='december'
    return mn
for i in range(12):
    inpNum=int(input())
    print(printMonth(inpNum))
