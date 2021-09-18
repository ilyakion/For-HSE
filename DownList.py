def DownList(l):
    if l=='':
        return l
    nl=""
    n=[l[0],1]
    for i in l[1:]:
        if n[0]==i:
            n[1]+=1
        else:
            if n[1]==1:
                nl+=n[0]
            else:
                nl+=str(n[1])
                nl+=n[0]
            n[0]=i
            n[1]=1
    if n[1]==1:
        nl+=n[0]
    else:
        nl+=str(n[1])
        nl+=n[0]
    n[0]=i
    n[1]=1
    return nl
