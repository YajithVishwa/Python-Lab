def Words():
    q=open('ex.txt','r')
    longg=''
    for line in q:
        if len(line)>len(longg):
            longg=line
    return longg
q=open("ex.txt","r")
print(Words())
