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
            b1=int(input('enter the no of ele to be inserted in nested list'))
            for k in range(b1):
                v=int(input('enter the value'))
                b.append(v)
                print(b)
            a.append(b)
            print(a)
        elif type=='s':
            c=set()
            c1=int(input('enter the no of ele to be inserted in nested set'))
            for l in range(c1):
                v=int(input('enter the value'))
                c.add(v)
                print(c)
            a.append(c)
            print(a)
        elif type=='d':
            e={}
            e1=int(input('enter the no of ele to be inserted in nested dict'))
            for q in range(e1):
                key=input('enter the key')
                value=input('enter the value')
                e[key]=value
                print(e)
            a.append(e)
            print(a)
        else:
            v=str(input('enter the value'))
            a.append(v)
            print(a)
dynlist()
            
            
