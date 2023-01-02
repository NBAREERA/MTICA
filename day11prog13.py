sample_dict={
    "name":"sumbol",
    "age":25,
    "salary":90000,
    "city":"New york"}
#keys to remove
keys=["name","salary"]
d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
print(d)
     
