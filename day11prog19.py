def Patternprinting(s,n):
    assert(n>=0),'INVALID'
    for i in range(n,0,-1):
        print(s*i)
s=input()
n=int(input())
try:
    Patternprinting(s,n)
except AssertionError as a:
    print(a)

