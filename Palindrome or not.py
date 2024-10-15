'''# Write a program to check the given number is Palindrome or not
n = int(input('Enter the number: '))
rev = 0
temp = n
while n!=0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
if temp == rev:
    print("the number is Palindrome ")
else:
    print("the number is not palindrome ")
'''