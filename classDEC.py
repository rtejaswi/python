def outer(a):
    print('add of a is ',a)
    print('in outer')
    def inner():
        print('in inner')
        a()
    return inner
@outer
class A:
    print('hi')
A()
print('end')
