def dyndict():
    a={}
    n=int(input('enter the no of ele to be inserted'))
    for i in range(n):
        key=input('enter the key')
        value=input('enter the value')
        a[key]=value
        print(a)
dyndict()
