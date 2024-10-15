# Write a program to check the given number is armstrong or not
'''n = int(input('Enter the number: '))
temp = n
sum = 0
c = len(str(n))
while n>0:
    rem = n % 10
    sum = sum+rem**c
    n = n // 10
if temp == sum:
    print('The given number is armstrong number ')
else:
    print('The given number is not armstrong number')'''


'''
# Wriet a program to check to the given number is armstrong or not in given range
for i in range(1, 100):
    n = i
    sum = 0
    c = len(str(n))
    while n != 0:
        rem = n % 10
        sum = sum + rem**c
        n = n // 10
    if i == sum:
        print(f'{i} is armstrong number ')'''