# fib
'''def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
nterms=int(input('enter'))
if nterms <= 0:
    print('invalide')
else:
    for i in range (nterms):
        print(fib(i))'''

#fact
'''def fact(n):
    if n < 0:
        print('input is wrong')
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n-1) 
print(fact(3))'''


'''nterms=int(input('enter'))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print('invalide')
elif nterms == 1:
    print(n1)
else:
    print('fib')
while count < nterms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1'''


'''def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))
nterms=int(input('enter'))
print('fibonacii sequence is')
if nterms <= 0:
    print('invalide')
else:
    for i in range(nterms):
        print(fib(i))'''



'''def fact(n):
    if n <= 1:
        return 1
    else:
        return(n * fact(n-1))
i=int(input('enter'))
if i<0:
    print('invalide')
else:
    print(fact(i))'''



# compound interest
'''def compound_interest(principle, rate, time):
    result = principle * (pow((1 + rate / 100), time))
    return result

p = float(input("Enter the principal amount: "))
r = float(input("Enter the interest rate: "))
t = float(input("Enter the time in years: "))
 
amount = compound_interest(p, r, t)
interest = amount - p
print("Compound amount is %.2f" % amount)
print("Compound interest is %.2f" % interest)'''



# Calorie calculator
'''CALORIES_PER_POUND = 3500

def main():
    try:
    	current_weight = float(input('please enter your current weight in pounds: '))
    	target_weight = float(input('please enter your target weight in pounds: '))
    	NumDays = int(input('please enter the number of days you have been on the diet: '))
    	calories_burned = float(input('please enter the number of calories you burn per day: '))
    except ValueError as err:
        print ("please enter a numeric value")
        return 
    
    calc_weight(current_weight, target_weight, NumDays, calories_burned)
    
def calc_weight(v, w, x, y):
    days_required = (v - w) * CALORIES_PER_POUND / y
    months_required = (days_required / 30)
    remaining_days = (days_required - x)
    remaining_months = (remaining_days / 30)
    pounds_remaining = ((v - w) - (y * x) / CALORIES_PER_POUND)
    pounds_burned = ((v - w) - pounds_remaining)
    
    print ('days required: ', days_required, 'months required: ', months_required, 'remaining days: ', remaining_days )
    print ('months remaining: ', remaining_months, 'pounds burned: ', pounds_burned, 'pounds remaining: ', pounds_remaining)
    
    
main()'''









 


 
