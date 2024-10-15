# write a program to check the given number is strong or not
n = int(input('Enter the number: '))
sum = 0
temp = n
while n!=0:
    rem = n % 10
    fact = 1
    for i in range(1, rem + 1):
        fact*=i
    sum+=fact
    n = n // 10
if temp == sum:
    print('The number is Strong number')
else:
    print('The number is Not Strong number')
