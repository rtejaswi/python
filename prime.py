def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return num, "is not a prime number"
    else:
        return num, "is a prime number"
num = int(input("enter a number: "))
print(prime(num))


'''n = int(input('enter the number: '))
for i in range(2,n):
    if n % i == 0:
        print('not a prime')
        break
else:
    print('prime')'''
courier new
