sample_dict={
    "name":"sumbol",
    "age":25,
    "salary":90000,
    "city":"New york"}
#keys to remove
keys=["name","salary"]
for k in keys:
     sample_dict.pop(k)
print(sample_dict)
