# Write a Python program to generate a list of prime numbers up to a given number.
n = int(input('Enter the number: '))
count = 0
for i in range(1,n+1):
        if n % i == 0:
            count+=1
if count == 2:
    print('The number is Prime number')
else:
    print('The number is not Prime number')