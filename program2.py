inpNum=int(input())
if inpNum<0:
    print("Even")
else:
    print("ODD")
'''
'''
def checkEven(n):
    if n<0:
        return "INVALID"
    if inpNum%2==0:
        return"Even"
    return"ODD"
inpNum=int(input())
print(checkEven(inpNum))

