def check(l,n):
   
    for i in l:
        if type(i)==list:
            check(i,n)
        else:
            n.append(i)
    return n
def flatten(aList):
    n=[]
    return check(aList,n)