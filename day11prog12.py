sample_dict={
    "name":"sumbol",
    "age":25,
    "salary":90000,
    "city":"New york"}
keys=["name","salary"]
res=dict()
for k in keys:
    res.update({k:sample_dict[k]})
print(res)
