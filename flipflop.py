a=int(input())
for i in range(a+1):
    if(i%3==0)and(i%5==0):
        print("FlipFlop")
    elif(i%3==0):
        print("Flip")
    elif(i%5==0):
        print("Flip")
    else:
        print(i)
    
