def sum_num(x):
    res=0
    for i in range(x+1):
        res=res+i
        #print("i=",i,"res=",res)
        yield("i=",i,"res=",res)
    return res
ob=sum_num(10)
for i in range(11):
    print(next(ob))
