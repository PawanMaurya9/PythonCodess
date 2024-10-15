# Write a program to print the given number is happy number or not
'''n = int(input('Enter the number: '))
temp = n
while n!=1 and n!=4:
    sum = 0
    while n!=0:
        rem = n % 10
        sum += rem**2
        n = n // 10
    n =sum
if n == 1:
    print('number  is a happy number')
else:
    print('number is not a happy number')
'''