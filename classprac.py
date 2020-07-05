#calculator
'''class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=cal(a,b)
choice=1
while choice!=0:
    print('----------------------------')
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print('----------------------------')
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==0:
        print("!!!...Exiting...!!!")
    else:
        print("Invalid choice!!")
print()'''

#area of rectangle

'''class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return ((2*self.breadth) + (2*self.length))
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())
print("Perimeter of rectangle:",obj.perimeter())
print()'''


# One Method Accepts a String from the User and Another Prints it
'''class print1():
    def __init__(self):
        self.string=""
 
    def get(self):
        self.string=input("Enter string: ")
 
    def put(self):
        print("String is:  ", self.string)
obj=print1()
obj.get()
obj.put()'''

# all possible subset of a set

class sub:  
    def f1(self, s1):  
        return self.f2([], sorted(s1))  
 
    def f2(self, curr, s1):  
        if s1:  
            return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])  
        return [curr]  

a=[]
n=int(input("Enter number of elements of list: "))
for i in range(n):
    b=int(input("Enter element: "))
    a.append(b)
print("Subsets: ")
print(sub().f1(a))


# area of circle

'''import math
class circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
 
r=int(input("Enter radius of circle: "))
obj=circle(r)
print("Area of circle:", round(obj.area(),2))
print("Perimeter of circle:", round(obj.perimeter(),2))'''

