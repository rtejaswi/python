n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if ((j==1 or j==5) and i!=5)or(i==5 and (j>1 and j<5)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
