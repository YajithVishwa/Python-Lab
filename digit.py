str=input()
zeros=0
ones=0
for i in range(0,len(str)):
  ch=str[i];
  if(ch=='0'):
    zeros=zeros+1
  else:
    ones=ones+1
    
if(zeros%2==1 or ones%2==1):
  print("YES",end="")
else:
  print("NO",end="")
