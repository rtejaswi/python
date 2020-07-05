# area of circle

from math import pi
class circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * (self.radius ** 2)
    def perimeter(self):
        return 2*pi * self.radius
    def __le__(self, others):
        return circle()
    def __add__(self, others):
        return circle()
r1=int(input("Enter radius of circle: "))
r2=int(input("Enter radius of circle: "))
oa=circle(r1)
ob=circle(r2)
x=oa.area()
y=ob.area()
a=oa.perimeter()
b=ob.perimeter()
print('area of circle 1 is :-  ', x)
print('area of circle 2 is :-  ', y)
print('area of perimeter 1 is :-  ', a)
print('area of perimeter 2 is :-  ', b)
print(x > y)
print(x + y)
print(a > b)
print(a + b)


#area of rectangle

'''class rectangle():
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length
    def area(self):
        return self.breadth * self.length
    def perimeter(self):
        return ((2 * self.breadth) + (2 * self.length))
    def __add__(self, others):
        return rectangle()
    def __ge__(self, others):
        return rectangle()
l1 = int(input("Enter length of rectangle1: "))
b1 = int(input("Enter breadth of rectangle1: "))
l2 = int(input("Enter length of rectangle2: "))
b2 = int(input("Enter breadth of rectangle2: "))
oa=rectangle(l1, b1)
ob=rectangle(l2, b2)
x=oa.area()
y=ob.area()
a=oa.perimeter()
b=ob.perimeter()
print("Area of rectangle1:- ", x)
print("Perimeter of rectangle1:- ", a)
print("Area of rectangle2:- ", y)
print("Perimeter of rectangle2:- ", b)
print(x < y)
print(x+y)
print(a < b)
print(a + b)'''
