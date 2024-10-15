'''n = int(input('Enter the number: '))
temp = n
sum = 0
while n!=0:
    rem = n % 10
    fact = 1
    for i in range(1, rem + 1):
        fact*=i
    sum+=fact
    n = n // 10
if temp == sum:
    print('the number is strong number')
else:
    print('the number is not strong')'''