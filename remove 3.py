lx=input()
l=lx.split(",")
i=0
for i in range(len(l)):
    if(i%3==0):
       l.remove(l[i])
print(l)
