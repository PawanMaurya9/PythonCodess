a = int(input("ENter the 1st number: "))
b = int(input("ENter the 2nd number: "))
if (b > a):

    print('b is greater then a ')
else:

    print('a is grater tha b')

    
a = 10
b = 20
if a > b:
    print(a,'is greater')
else:
    print(b,'is greater')
print('out if else block')

a = 100
b = 150
if b > a:
    print(b, 'is greater than a')
else:
    print(a, 'is greater than b')

num1 = int(input(f"Enter the first number: "))
num2 = int(input(f"Enter the second number: "))
if num1 > num2 :
    print(f"Num1 is grater than num2: ")
else:
    print("num2 is greater than num1: ")


a = int(input(f"Enter the first number: "))
b = int(input(f"Enter the second number: "))
c = int(input(f"Enter the third number: "))
if a > b and b > c:
    print(f"{a} is greater ")
elif b > c:
    print(f"{b} is greater ")
else:
    print(f"{c} is greater ")