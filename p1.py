n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==5)or(j==3)or(i==4 and (j>1 and j<5))or (i==3 and (j>1 and j<5)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
