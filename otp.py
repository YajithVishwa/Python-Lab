import math,random
otp=""
digits="0123456789"
for i in range(4):
    otp+= digits[math.floor(random.random()*10)]
print(otp)
