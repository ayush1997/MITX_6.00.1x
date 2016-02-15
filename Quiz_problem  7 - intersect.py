def dict_interdiff(d1, d2):
    newdic1 = {}
    newdic2={}
    t = ()
    for i in d1:
        if i in d2:
            newdic1[i]=f(d1[i],d2[i])
    t = t+(newdic1,)
    for i in d1:
        if i not in d2:
            newdic2[i] = d1[i]
    for j in d2:
        if j not in d1:
            newdic2[j] = d2[j]
    t = t+(newdic2,)
    return t 
        
            