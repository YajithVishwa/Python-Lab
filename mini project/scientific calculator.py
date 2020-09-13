def switch(n):
    if(n=="1"):
        arthematic()
    elif(n=="2"):
        logical()
    elif(n=="3"):
        comparison()
    elif(n=="4"):
        bitwise()
    elif(n=="5"):
        trignomentry()
    elif(n=="6"):
        factorial()
    elif(n=="7"):
        factor()
def arthematic():
    l=[]
    print("\nEnter the value with spaces")
    l=[int(x) for x in input().split()]
    n=input("\n1.add,2.sub,3.mul,4.div,5.expo,6.floor,7.Square root")
    if(n=="1"):
        g=0
        for i in range(len(l)):
            g+=l[i]
        print("\nSum of ",l,"is",g)
    elif(n=="2"):
        g=0
        for i in range(len(l)):
            g+=l[i]
        print("Difference of ",l,"is",g)
    elif(n=="3"):
        g=0
        for i in range(len(l)):
            g*=l[i]
        print("Product of ",l,"is",g)
    elif(n=="4"):
        g=0
        for i in range(len(l)):
            g/=l[i]
        print("Divisor of ",l,"is",g)
    elif(n=="5"):
        g=l[0]
        for i in range(len(l)):
            g**=l[i]
        print("Exponent of ",l,"is",g)
    elif(n=="6"):
        g=0
        for i in range(len(l)):
            g//=l[i]
        print("Floor divison of ",l,"is",g)
    elif(n=="7"):
        import math
        a=int(input("\nValue for finding square root"))
        print("Square root of",a,"is",math.sqrt(a))
    else:
        print("Invalid input,Run the program again")
def logical():
    x=input("\n1.True or 2.False")
    y=input("\n1.True or 2.False")
    if(x=="1")and(y=="1"):
        x=True
        y=x
    elif(x=="0")and(y=="0"):
        x=False
        y=x
    elif(x=="1"):
        x=True
    elif(y=="1"):
        y=True
    elif(x=="0"):
        x=False
    else:
        y=False
    print("x and y is",x and y)
    print("x or y is",x or y)
    print("not x is",not x)
    print("not y is",not y)
def comparison():
    l=[]
    g=0
    ls=0
    e=0
    n=0
    print("\nEnter the values")
    l=[int(x) for x in input().split()]
    for i in range(len(l)):
        g=(g>l[i])
        n=(n!=l[i])
        ls=(ls<l[i])
        e=(e==l[i])
    print("Less than",ls)
    print("Greater than",g)
    print("Equal to",e)
    print("Not equal to",n)
def bitwise():
    x=int(input("\nEnter the value in binary"))
    y=int(input("\nEnter the value in binary"))
    print("&",x&y)
    print("|",x|y)
    print("-",x-y)
    print(">>",x>>y)
    print("<<",x<<y)
def trignomentry():
    import math
    a=int(input("\nEnter the value"))
    print("sin",math.sin(a))
    print("cos",math.cos(a))
    print("tan",math.tan(a))
    d=input("\nDo you want to find hypotenuse?")
    if(d=="yes")or(d=="Yes")or(d=="YES"):
        b,c=input("Enter the value of a and b").split()
        b=int(b)
        c=int(c)
        print(math.hypot(b,c))
    print("\nRadian",math.radians(a))
def factorial():
    n=int(input("\nEnter the value to find the factorial"))
    l=[0,1]
    for i in range(n+1):
        s=l[i]+l[i+1]
        l.append(s)
    print("The factorial is")
    print(l,end=" ")
def factor():
    x=int(input("\nEnter the value for factor"))
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
       if (x % i == 0):
           print(i)
print("\nEnter the number")    
n=input("\n1.arthematic,2.logical,3.comparison.4.Bitwise,5.Trignomentry,6.Factorial,7.Factors")
switch(n)
