def checkAnagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return 'it is a palindrom'
    else:
        return 'it is not palindrome'
    
inp=input().split()
print(checkAnagram(inp[0],inp[1]))
