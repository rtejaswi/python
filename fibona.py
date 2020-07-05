fib = []

n = int(input('Enter the number: '))

print("the first {} fibonacci number are : ".format(n))

fib.append(0)
fib.append(1)

for i in range(1, n):
    num = fib[i] + fib[i-1]

    fib.append(num)

for j in fib:
    print(j)
