def single(cls):
    print('cls is in:-  ',cls)
    i={}
    print(i)
    def inner():
        if cls not in i:
            print('hi')
            i[cls]=cls()
        return i[cls]
    return inner
@single
class A:
    pass
a = A()
b = A()
print('object a:-', a)
print('object b:-', b)
