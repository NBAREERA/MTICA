##def printSeries(ch,n):
##    sp='.'
##    for i in range(0,n):
##        print(sp*(n-i-1)+ch*(2*i+1)+sp*(n-i-1))
##    return None
##inpch=input()
##inpNum=int(input())
##printSeries(inpch,inpNum)
##    
n=int(input())
if n<0:
    print('INVALID')
else:
    for i in range(n):
        print('.'*(n-i-1)+'*'*((i*2)+1)+'.'*(n-i-1))
