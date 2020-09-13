r,c = input().split()
k=1
m = int(r)
n = int(c)
for i in range(m):
  for j in range(n):
    if( j != n-1):
      print(k,end=" ")
    else:
      print(k)
    k=k+1
