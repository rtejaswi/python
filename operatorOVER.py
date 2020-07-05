class A:
    
    def __init__(self,x):
        self.x = x
    def __add__(self,others):
        return self.x + others.x
a = A(7)
b = A(3)
print(a+b)
