def upper_d(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner
def split_d(func):
    def wrapper():
        str2 = func()
        return str2.split()
    return wrapper
@split_d
@upper_d
def smart():
    return "good morning"
print(smart())



'''def outer(func):
    print('add of outer', outer)
    print('add of func', func)    
    def inner():
        #print('inside inner')
        print('add of inner', inner)
        func()
    return inner
@outer
def smart():
    #print('inside smart')
    print('add of smart', smart)
smart()'''
