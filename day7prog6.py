ans=[]
for i in range(100,111):
    a=i
    temp=[]
    for j in range(1,10):
       if a%j==0:
          temp.append(j)
    ans.append([i,max(temp)])
print(a,':',max(temp),'temp:',temp)
