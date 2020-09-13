class square():
    def area(self,a):
        print("Area of square is",a*a)
    def perimeter(self,a):
        print("Perimeter of square is",4*a)
class retangle():
    def area(self,l,b):
        print("Area of rectangle is",l*b)
    def perimeter(self,l=4,b=6):
        print("Perimeter of retangle is",2*l+b)
sq=square()
rec=retangle()
sq.area(4)
sq.perimeter(4)
rec.area(3,4)
rec.perimeter()
