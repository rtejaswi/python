def dynlist():
    a=[]
    n=int(input('enter the no of ele to be inserted'))
    for i in range(n):
        type=input('enter the type of ele')
        if type=='i':
            v=int(input('enter the value'))
            a.append(v)
            print(a)
        elif type=='f':
            v=float(input('enter the value'))
            a.append(v)
            print(a)
        elif type=='l':
            b=[]
            b1=int(input('enter the ele to be inserted in nested list'))
            for k in range(b1):
                v=int(input('enter the value'))
                b.append(v)
                print(b)
            a.append(b)
            print(a)
        else:
            v=str(input('enter the value'))
            a.append(v)
            print(a)
dynlist()
            
            
