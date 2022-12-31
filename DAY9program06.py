fo=open(r"D:\pythonpractice60\Day09\abc.txt","W+")
inpStr=input('Enter text:')
fo.write(inpStr)
inpStr=input('Enter text:')
fo.write(inpStr)

fo.close()
print('Text written to File')
