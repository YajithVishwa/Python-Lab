l1=[]
l2=[]
l3=[]
l4=[]
n=int(input())
for i in range(n):
    l1.append(i)
for i in range(len(l1)):
    if(l1[i]%2!=0)and(l1[i]%3!=0)and(l1[i]%5!=0):
        l2.append(i)
        l2.append(2)
        l2.append(3)
        l2.append(5)
    elif(l1[i]%2==0):
            l3.append(i)
    elif(l1[i]%2!=0):
            l4.append(i)
print("The prime numbers are",l2)
print("The odd numbers are",l4)
print("The even numbers are",l3)
