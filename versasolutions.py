# sorting alphabetically

istr = input('e')
ws = istr.split(',')
ws .sort()

print('the sorted words are')
for w in ws:
    j = ','.join(ws)
print(j)

# min no of appends needed to a string palindrome

def ispal(Str):
    Len = len(Str)
    if (Len == 1):
        return True
    ptr1 = 0
    ptr2 = Len - 1

    while(ptr2 > ptr1):
        if (Str[ptr1] != Str[ptr2]):
            return False
        ptr1 += 1
        ptr2 -= 1
    return True
def nofapp(s):
    if(ispal(s)):
        return 0
    del s[0]
    return 1 + nofapp(s)
se = input('enter the syring')
s = [i for i in se]
print(nofapp(s))

#Robot

s = int(input('enter the steps'))
c = 1
if s % 5 == 0:
    q = s // 5
    print(q)

else:
    q = s // 5
    c = q + 1
    print(c)

    
    
    
