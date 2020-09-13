import os
 
with open('ex.txt', 'rb') as f:
    f.seek(-2, os.SEEK_END)
    while f.read(1) != b'\n':
        f.seek(-2, os.SEEK_CUR) 
    k=(f.readline().decode())
    g=open("ex9.txt","w")
    g.write(k)
    g.close()
    f.close()
