def is_strong_number(number):
    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    sum = 0
    temp = number
    while number != 0:
        rem = number % 10
        sum += factorial(rem)
        number //= 10
    return temp == sum
n = int(input('Enter the number: '))
if is_strong_number(n):
    print('The number is a Strong number')
else:
    print('The number is Not a Strong number')