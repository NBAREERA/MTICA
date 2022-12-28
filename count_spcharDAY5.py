def extract_spchar(s):
    spchar=''
    for i in s:
         if i in '@#%^&*><':
             spchar+=1
    return spchar

str1=input()
a=extract_spchar(str1)
print("no of special character in:'",str1,"'is",a)

