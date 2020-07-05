'''a=[1,2,3,4,5]
i=0
while i<len(a):
    print('*'*a[i],end=' ')
    i+=1
    print()'''

'''i=[1,2,3,4,5]
for x in i:
    print(x*'*')'''

'''n=5
a=ord('A')
b=1
for i in range(1,n+1):
    #a=ord('A')
    #b=1
    for j in range(1,n+1):
        if i<=j:
            if i%2==0:
                print(b,end=' ')
            else:
                print(chr(a),end=' ')
            a+=1
            b+=1
        else:
            print(' ',end=' ')
    print()
    #a+=1
    #b+=1'''


'''n=5
a=ord('A')
b=1
for i in range(1,n+1):
    #a=ord('A')
    #b=1
    for j in range(1,n+1):
        if i<=j:
            print(chr(a),end=' ')
            #a+=1
        else:
            print(' ',end=' ')
    print()
    #a+=1
    #b+=1'''


'''s=0
p=7
n=4
#a=ord('A')
b=4
for i in range(n):
    #a=ord('A')
    #b=1
    for j in range(s):
        print(' ',end=' ')
    for k in range(p):
        print(b,end=' ')
        if k>=p//2:
            b+=1
        else:
            b-=1
    print()
    s+=1
    p-=2
    b-=2'''


'''s=3
p=1
n=7
#a=ord('A')
#b=1
for i in range(1,n+1):
    a=ord('A')
    #b=1
    for j in range(s):
        print(' ',end=' ')
    for k in range(p):
        if k==0 or k==p-1:
            print('*',end=' ')
        elif k>0 or k>p-1:
            print(chr(a),end=' ')
            if k>=p//2:
                a-=1
            else:
                a+=1
        else:
            print(' ',end=' ')
    if i<=n//2:
        s-=1
        p+=2
    else:
        s+=1
        p-=2
    print()'''



'''s=3
p=1
n=5
a=ord('A')
for i in range(1,n+1):
    for j in range(s+1):
        print(' ',end=' ')
    for k in range(p):
        if k==0 or k==p-1:
            print(chr(a),end=' ')
        elif i==5:
                a-=1
                print(chr(a),end=' ')
        else:
            print(' ',end=' ')
    print()
    s-=1
    p+=2
    a+=1'''


'''# Python3 code to demonstrate working of 
# Extracting Kth Key in Dictionary 
# Using keys() + list() 

# initializing dictionary 
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3} 

# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 

# initializing K 
K = int(input('Enter the value of K:- '))

# Using keys() + list() 
# Extracting Kth Key in Dictionary 
res = list(test_dict.keys())[K] 

# printing Kth key 
print("The Kth key of dictionary is : " + str(res))''' 

        
