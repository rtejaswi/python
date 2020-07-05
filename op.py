# factorial ===================================================================================
'''from math import factorial as f
n = int(input('enter the range'))
for i in range(n+1):
    factorial = f(i)
    print(factorial)'''

# Access specifiers    =============================================================

'''class A:
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c
    def disp(self):
        print('a = ', self.a)
        print('b = ', self._b)
        print('c = ', self.__c)
class B(A):
    def disp(self):
        print('a = ', self.a)
        print('b = ', self._b)
        print('c = ', self._A__c)

oa = A(1, 2, 3)
oa.disp
ob = B(10, 20, 30)
ob.disp'''

# Constructor chining  ===========================================================

'''class A:
    a = 10
    def __init__(self, x):
        self.x = x
class B(A):
    b = 20
    def __init__(self, y, x):
        self.y = y
        A.__init__(self, x)
        #super().__init__(x)
    def disp(self):
        print('y = ', self.y)
        print('x = ', self.x)
ob = B(12, 13)
ob.disp'''

# packinf & unpacking  ==========================================================

'''def disp(*args):
    print(args)
    print(*args)
def packing(*args):
    disp(*args)
packing('welcome', 'to', 'python')'''
#++++++++++++++++++++++++++++++++++++++++++++
'''a =[1, 2]
def unpacking(a = None, b = None, c = None):
    print(a)
    print(b)
    print(c)
unpacking(*a)'''

# singleton class  ==============================================================

'''def single(cls):
    i = {}
    def inner():
        if cls not in i:
            i[cls] = cls()
        return i[cls]
    return inner
@single
class A:
    pass
oa1 = A()
oa2 = A()'''

# operator overloading  =========================================================

'''from math import pi
class circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return (pi * (self.r ** 2))
    def __lt__(self, others):
        return circle()
    def __add__(self, others):
        return circle()
r1 = int(input('enter the radius'))
r2 = int(input('enter the radius'))
oa1 = circle(r1)
oa2 = circle(r2)
x = oa1.area()
y = oa2.area()
print(x > y)
print(x + y)'''

#  has a relationship  ==========================================================

class A:
    a = 10
class B(A):
    oa = A()
    b = 20
ob = B()

# iterator FIB ==================================================================

'''class F:
    def __init__(self, mnv, mxv):
        self.min = mnv
        self.max = mxv
    def __iter__(self):
        return self
    def __next__(self):
        def fib(n):
            if n<=1:
                return n
            else:
                return (fib(n-1)+fib(n-2))
        nterms=int(input('enter'))
        if nterms<=0:
            print('invalide')
        else:
            for i in range (nterms):
                print(fib(i))
        if self.min<=self.max:
            r = fib(self.min)
            self.min+=1
            return r
        raise StopIteration
m = int(input('enter the max value'))
oa = F(0, m)
x = F.__iter__(oa)
for i in range(m):
    print(F.__next__(x))'''

# fib   ===================================================

'''def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
nterms=int(input('enter'))
if nterms<=0:
    print('invalide')
else:
    for i in range (nterms):
        print(fib(i))'''



n = int(input('enter the number'))
rev = 0
while(n > 0):
    a = n % 10
    rev = rev  * 10 + a
    n = n // 10
    print(rev)

'''n = input('enter the number')
re = n[::-1]
if n.isdigit() == True:
    print(int(re))
elif n[0] == '-':
    r = re.replace('-', ' ')
    print('+' + r)'''
