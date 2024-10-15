# Write a Python program to check if a number is a palindrome.
n = int(input('Enter the number: '))
temp = n
rev = 0
while n!=0:
    rem = n % 10
    rev = rev*10+rem
    n = n // 10
if temp == rev:
    print(f'The number is Palindrome rev: {rev}')
else:
    print(f'The number is not Palindrome rev: {rev}')