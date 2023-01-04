def PrintBlue():
    print('you chose blue!\n')
    return
def PrintRed():
    print('you chose red!\n')
    return
def PrintOrange():
    print('you chose orange!\n')
    return
def PrintYellow():
    print('you chose yellow!\n')
def choice():
    print("0:Blue")
    print("1:Red")
    print("2:Orange")
    print("3:Yellow")
    print("4:Quit")
    return
ColorSelect={0:PrintBlue,1:PrintRed, 2:PrintOrange,
             3:PrintYellow}
selection=0
while True:
    if selection==4:break
    choice()
    selection=int(input("select a color option:"))
    if(selection>=0)and(selection<4):
        ColorSelect[selection]()
