def armstrong_number(n):
    temp = n
    sum = 0
    c = len(str(n))
    while n>0:
        rem = n % 10
        sum = sum+rem**c
        n = n // 10
    return sum
n = int(input('Enter the number: '))
if armstrong_number(n):
    print('The given number is armstrong number ')
else:
    print('The given number is not armstrong number')