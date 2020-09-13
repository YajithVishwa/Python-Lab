def revs(str):
    for i in range(0,len(str)):
        print(str[i],end="")
    print()
    for j in range(len(str)-1,-1,-1):
        print(str[j],end="")
def union(str1,str2):
    str3=0
    i=0
    for str1 in str2:
        str3[i]=str1
        i+=1
    print(str3)
    return
str=input()
str1=input()
str2=input()
print(revs(str))
print(union(str1,str2))
    
