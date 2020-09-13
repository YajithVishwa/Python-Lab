class triangle(): 
    def area(self):
        a=10
        b=20
        c=(a*b)/2
        print("Area of triangle is",c) 
  
    def perimeter(self):
        a=10
        b=20
        c=30
        d=a+b+c
        print("Perimeter of triangle",d)   
class frustum(): 
    def area(self):
        import math
        pi=math.pi
        r=10
        R=20
        l=10
        c=pi*l*(R+r)
        print("Curved surface area of frustum",c) 
    def perimeter(self): 
        print("Volume of frustum")
        import math
        pi=math.pi
        r=10
        R=20
        l=30
        h=30
        c=1/3*pi*h*(r*r+R*R+r*R)
        print("Volume of frustum",c)
tr=triangle()
fr=frustum()
for c in (tr,fr): 
    c.area() 
    c.perimeter() 
