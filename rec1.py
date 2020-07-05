def rec(string):
    if len(string)==1: 
        return
    t=string[0] 
    rec(string[1:]) 
    print(t,end='')
string = 'KARMA'
print(string,end='')
rec(string) 
