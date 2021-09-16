def sfdsdf(n):
    a=''
    if n%3 == 0:
        a+='Pling'
    if n%5 == 0:
        a+='Plang'
    if n%7 == 0:
        a+='Plong'
    if n%3==0 and n%5==0 and n%7==0:
        a+=str(n)
    return a