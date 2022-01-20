class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        area=self.l*self.b
        print("Area of rectangle :",area)
        return(area)
    def perimeter(self):
        per=2*(self.l+self.b)
        print("Perimeter of rectangle :",per)
        return(per)
r1=rectangle(6,7)
r2=rectangle(8,9)
a=r1.area()
r1.perimeter()
b=r2.area()
r2.perimeter()
if(a>b):
    print("Rectangle one isgreater :",a)
else:
    print("Rectangle two is greater :",b)
