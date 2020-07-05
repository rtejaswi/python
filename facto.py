fact = []

fact.append(1)
fact.append(1)

n = int(input('enter the number'))

print('the first {} factorial series are : '.format(n))

for i in range(1, n):
    num = fact[i]*(i+1)

    fact.append(num)

for j in fact:
    print(j)
