'''n=5
for i in range(1,n+1):
    k=ord('Z')
    for j in range(1,n+1):
        if i<=j:
                print(chr(k),end=' ')
                k-=1
        else:
            print(' ',end=' ')
           
    print()'''


'''n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<=6:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''n=5
for i in range(1,n+1):
    k=1
    p=ord('A')
    for j in range(1,n+1):
        if i+j<=6:
            if i==j:
                print(k ,end=' ')
                k+=1
            else:
                print(chr(p),end=' ')
                p+=1
        else:
            print(' ',end=' ')
    print()'''
   
    
    
    
     
    
