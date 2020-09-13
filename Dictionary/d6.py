d={1:0,2:1,3:2}
d1={4:3,5:4,6:5}
d2={}
for i in range(len(d)):
    d2={**d,**d1}
print(d2)
