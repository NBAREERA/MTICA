ans=[]
for i in range(1,10):
    if (i%2==0 or 1%3==0 or i%4==0 or i%8==0 or i%9==0):
     ans.append(i)
print(ans)

ans=[i for i in range(1,10)  if (i%2==0 or 1%3==0 or i%4==0 or i%8==0 or i%9==0)]
print(ans)

