##def solveProblem(s):
##    lst=s.split()
##    return(len(i) for i in lst)
##inp=input()
##solveProblem=[i:i[::-1] for i in lst]
##print(*solveProblem)
##inp1=['papaya','coconut','grapes','banana']
def reverseString(s):
    ans=[i[::-1] for i in s]
    return ans
inp=input().split()
print(*reverseString(inp))
