s = 4
p = 1
a = ord('A')
n=5
for i in range(1, n+1):
    if i<n:
        for j in range(s+2):
            print(' ', end = ' ')
        for k in range(p+2):
            if k == 1 or k == p-1:
                print(chr(a), end = ' ')
            else:
                print(' ', end = ' ')
        a+=1
    else:
        m = 8
        b = ord('E')
        for k in range(1, n+5):
            print(chr(b), end = ' ')
            if k<=p//2:
                b-=1
            else:
                b+=1
    print()
    s-=1
    p+=1
