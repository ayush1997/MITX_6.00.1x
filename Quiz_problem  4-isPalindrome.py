def isPalindrome(aString):

    a = ""
    for i in range(len(aString)-1,-1,-1):
        a = a+aString[i]
    if a == aString:
        return True
    else:
        return False
    

