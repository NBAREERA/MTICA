def PrintSunday():
    print('sunday')
    return
def PrintTuesday():
    print('tuesday')
    return
def PrintSaturday():
    print('saturday')
    return
def PrinMonday():
    print('monday')
    return
def PrintWednesday():
    print('wednesday')
def choice():
    print("enter day number 1-7")
dayDict={1:PrintSunday,2:PrinMonday, 3:PrintTuesday,
             7:PrintSaturday}
choice()
dayno=int(input())
if(dayno>=1 and dayno<=7):
    dayDict[dayno]()
else:
    print(dayno)



