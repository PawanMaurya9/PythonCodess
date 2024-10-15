def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count == 2
x = int(input("Enter the first number: "))
if is_prime(x):
    print('The given number is a prime number')
else:
    print('The given number is not a prime number')