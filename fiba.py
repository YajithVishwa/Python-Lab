fiba=int(input())
l=[]
l1=0
for i in range(0,fiba+1):
    l1=l[i]+l[i+1]
    l.append(l1)
print(l)
