def fib(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
         return num*fib(num-1)
num = int(input("enter thwe number : "))
for i in range(1, num+1):
    print(fib(i))
