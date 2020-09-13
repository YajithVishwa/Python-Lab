def occ():
    str=input()
    w=input()
    count=0
    for i in range(len(str)-1):
        if(w==str[i]):
            count+=1
    print(count)
def circle():
    import math
    rad=float(input())
    pi=math.pi
    area=4*pi*(rad*rad)
    return area
def small():
    a=int(input())
    b=int(input())
    c=int(input())
    if(a<b)and(a<c):
        return ("a is small")
    elif(b<c):
        return ("b is small")
    else:
        return ("c is small")
def fibo():
    l=[]
    a=int(input())
    b=int(input())
    n=int(input())
    l.append(a)
    l.append(b)
    for i in range(n):
        c=l[i]+l[i+1]
        l.append(c)
    return l
n=input("occ\ncircle\nsmall\nfibo\n")
if(n=="occ"):
    occ()
elif(n=="circle"):
    print(circle())
elif(n=="small"):
    print(small())
elif(n=="fibo"):
    print(fibo())
    
