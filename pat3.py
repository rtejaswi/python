n=5
for i in range(1,n+1):
    k=ord('E')
    for j in range(1,n+1):
        if i<=j:
                print(chr(k),end=' ')
                k-=1
        else:
            print(' ',end=' ')
           
    print()
   
    
    
    
     
    
