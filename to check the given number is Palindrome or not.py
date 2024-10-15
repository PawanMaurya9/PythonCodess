# Write the program to check the given number is Palindrome or not
n  = int(input('Enter the number: '))
rev = 0
temp = n
while n!=0:
    rem = n % 10
    rev = rev*10+rem
    n = n // 10
if temp == rev:
    print('The number is Palindrome')
else:
    print('The number is Not a Palindrome')