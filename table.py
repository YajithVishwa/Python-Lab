def mul(n,m):
    d1={}
    for i in range(1,m+1):
        d1[i]=i*n
    return d1
n=int(input("Enter the multiplication table"))
m=int(input("Enter the table limit"))
print(mul(n,m))
