class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length  *self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)
l=int(input("length of 1st rectangle:"))
b=int(input("breadth of 1st rectangle:"))
r1=Rectangle(l,b)
print("Area:",r1.area())
print("Perimeter:",r1.perimeter())

l=int(input("length of 2nd rectangle:"))
b=int(input("breadth of 2ndrectangle:"))
r2=Rectangle(l,b)
print("Area:",r2.area())
print("Perimeter:",r2.perimeter())

if r1.area() > r2.area():
    print("1st Rectanlgle is greater")

else:
    print("2nd Rectangle is greater")
