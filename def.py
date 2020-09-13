def add(d1):
    d2={}
    v=int(input("Enter the value to be added"))
    for i in range(1,len(d1)+1):
        d2[i]=d1[i]+v
    return d2
def dele(d1):
    k=int(input("index to be deleted"))
    d1.pop(k)
    n=int(input("Index value"))
    r=int(input("Value to be added"))
    d1[n]=r
    return d1
def le(d1):
    return len(d1)
def cpy(d1):
    d3={}
    d3=d1
    print(d3)
    return d3
def de(d1):
    del d1
    print(d1)
    return
d1={}
p=int(input("Enter the dictionary length"))
for i in range(1,p+1):
    d1[i]=i
o=input("add,dele,le,cpy,de")
if(o=="add"):
    print(add(d1))
elif(o=="dele"):
    print(dele(d1))
elif(o=="le"):
    print(le(d1))
elif(o=="cpy"):
    print(cpy(d1))
elif(o=="de"):
    print(de(d1))
