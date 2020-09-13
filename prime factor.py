a=int(input("Enter the number"))
l1=[]
i=1
while(i<=a):
    if a%i==0:
        l1.append(i)
        i+=1
    else:
        a//=i
print(l1)
    
    
