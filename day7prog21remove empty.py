#remove empty strings
lst1={"sedan","suv","","","pickup",'',' '}
ans=[i for i in lst1 if i]
for i in lst1:
    if i:
        ans.append(i)
print(ans)
