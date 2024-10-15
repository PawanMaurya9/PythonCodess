#Write a Python program to check the given number is prime or not
x = int(input("Enter the first number: "))
count = 0
for i in range(1,x+1):
    if x % i == 0:
        count+=1
if count == 2:
    print('The given no. is prime number')
else:
    print('The given no. is not prime number')
#output
'''Enter the first number: 5
The given no is prime number'''