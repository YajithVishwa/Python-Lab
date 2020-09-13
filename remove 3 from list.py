l1=[int(x) for x in input().split()]
i=0
for i in range(len(l1)):
    if(l1[i]%3==0):
        l1.pop()
print(l1)
