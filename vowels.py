l=['a','b','c','d','e','f','g','h','i','j','k']
l1=[]
l2=[]
for i in range (0,len(l)+1):
    if (l[i]=="a"or l[i]=="e"or l[i]=="i"or l[i]=="o"or l[i]=="u"):
        l1.append(l[i])
    else:
        l2.append(l[i])
print(l2)

