sample_dict={
    "name":"sumbol",
    "age":25,
    "salary":90000,
    "city":"New york"}

sample_dict['location']=sample_dict.pop('city')
print(sample_dict)
#keys to remove
##keys=["name","salary"]
##d=dict()
##for i in sample_dict.keys()-keys:
##    d[i]=sample_dict[i]
##print(d)
     
