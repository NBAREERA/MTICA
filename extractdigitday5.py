def extractDigit(s):
    Digit=''
    for i in s:
        if i in '0123456789':
            Digit+=i
    return Digit
str1=input()
a=extractDigit(str1)
print("digits in:'",str1,"'is",a)
