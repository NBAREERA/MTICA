def PrintJanuary():
    print('january')
    return
def PrintFebruary():
    print('february')
    return
def PrintMarch():
    print('march')
    return
def PrinApril():
    print('april')
    return
def PrintMay():
    print('may')
def choice():
    print("enter month number 1-4")
monthDict={1:PrintJanuary,2:PrintFebruary, 3:PrintMarch,
             4:PrinApril,5:PrintMay}
choice()
monthno=int(input())
if(monthno>=1 and monthno<=5):
    monthDict[monthno]()
else:
    print('INVALID')



