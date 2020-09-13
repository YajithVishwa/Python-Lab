d={}
c=[]
for i in range(1,16):
    d.update({i:i*i})
    c.append(d.get(i))
f=0
for i in range(len(c)):
    f+=c[i]
print(f)
