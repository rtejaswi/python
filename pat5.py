num=1
space=3
n=4
for i in range(1,n+1):
    a=1
    for j in range(space):
        print(' ',end=' ')
    for k in range(num):
        print(a,end=' ')
        if k>=num//2:
            a-=1
        else:
            a+=1
    print()
    num+=2
    space-=1
