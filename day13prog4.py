def PrintSunday():
    print('you chose sunday!\n')
    return
def PrintTuesday():
    print('you chose tuesday!\n')
    return
def PrintSaturday():
    print('you chose saturday!\n')
    return
def PrinMonday():
    print('you chose monday!\n')
    return
def PrintWednesday():
    print('you chose wednesday!\n')
def choice():
    print("1:Sunday")
    print("2:Monday")
    print("3:Tueday")
    print("7:Saturday")
    print("4:Wednesday")
    print("5:Quit")
    return
daySelect={1:PrintSunday,2:PrinMonday, 3:PrintTuesday,
             7:PrintSaturday}
selection=0
while True:
    if selection==5:break
    choice()
    selection=int(input("select a day option:"))
    if(selection>=0)and(selection<5):
         daySelect[selection]()


