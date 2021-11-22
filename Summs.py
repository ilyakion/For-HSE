def plus(n, a):
    for i in range(len(n)):
        n[i]+=a
    return n

def F(n,k):
    m = []
    if len(n)>=k:
        if k==1:
            for i in range(k-1, len(n)):
                m.append(n[i])
        elif k==2:
            for i in range(k-1, len(n)):
                m.append(n[0]+n[i])
            m += F(n[1:], k)
        else:
            for i in range(k-1, len(n)):
                m += plus(F(n[1:],k-1),n[0])
    return m

def unic(n):
    m = []
    for i in n:
        if not(i in m):
            m.append(i)
    m.sort()
    return m

def sums(n):
    m = [0]
    for i in range(1,len(n)+1):
        m += (F(n,i))
    m = unic(m)
    return len(m)
