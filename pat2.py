n=5
for i in range(1,n+1):
    k=ord('A')
    b=2
    for j in range(1,n+1):
        if i>=j:
            if j%2==0:
                print(b,end=' ')
                b+=2
            else:
                 print(chr(k),end=' ')
                 k+=2
        else:
            print(' ',end=' ')
    print()
    
    
     
    
