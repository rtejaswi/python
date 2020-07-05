#Access specifiers
'''class A:
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c
    def disp(self):
        print('a is',self.a)
        print('b is',self._b)
        print('c is',self.c)
class B(A):
    def disp(self):
        print('a is',self.a)
        print('b is',self._b)
        print('c is',self._c)
ob = A(10, 20, 30)
ob.disp()'''


#const chining
'''class A:
    a = 10
    def __init__(slef):
        print('in init')
class B(A):
    b = 10
    def __init__(self):
        print('in child')
        #A.__init__(self)
        super().__init__()
ob = B()'''


#packing
'''def disp(*args):
    print(args)
    print(*args)
def packing(*args):
    print('insid generic method')
    disp(*args)
packing('Welcom', 'to', 'pyhton', 'class')'''



#unpacking
'''a = [1, 2]
def unpacking(a = None,b = None,c = None):
    print(a)
    print(b)
    print(c)
unpacking(*a)'''


#has a relationship
'''class A:
    a = 10
    def disp(self):
        print('in parent class')
class B(A):
    oa = A()
    b = 20
    def disp(self):
        print('in child class')
ob = B()
ob.disp()
print(B().a)
print(B().b)
print(A().a)'''

#fib in iter
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


#prime
'''def prime(num):
    for i in range(2, num):
        if num % i == 0:
           return'not a prime'
        else:
            return'is a prime'
num = int(input('enter the number'))
print(prime(num))'''

#function decorator mail
'''def mail(func):
    def rec(name):
        print('Dear', name)
        func()
        print('Thankyou \n Manager')
        print('******************')
    return rec
print('rrrrrrrrrrrrrrrr')
@mail
def manager():
    print('This is to inform that there is a holiday')
    print('On yhe special occation of christmas')
a = ['Tejaswi', 'Naveen', 'Varun', 'Vicky']
for i in a:
    manager(i)'''
#yield
'''def gen(n):
    i = 1
    while i<=n:
        r = i**3
        yield r
        i+=1
n=gen(5)
j=iter(n)'''
#yield factorial
def gen(m):
    i = 1
    while i<=m:
        r = fact(i)
        yield r
        i+=1
def fact(n):
    if n  in [0, 1]:
        return 1
    else:
        return n * fact(n-1)
y = gen(5)
j = iter(y)
