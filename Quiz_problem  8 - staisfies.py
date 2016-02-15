def satisfiesF(L):
    n = []
    
    for i in L:
        if f(i)==True:
            n.append(i)
    L=n
    return len(n)
            
            
run_satisfiesF(L, satisfiesF)