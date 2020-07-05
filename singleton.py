def singleton(cls):
    print('add',cls)
    i={}
    print(i)
    def inner():
        if cls not in i:
            print('hi')
            i[cls]=cls()
        return i[cls]
        
    return inner
@singleton
class A:
    pass
A()
print(A)
oa = A()
ob = A()
oc = A()
