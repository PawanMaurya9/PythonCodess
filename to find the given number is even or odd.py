num1 = float(input(f"Enter the first numbers: "))
num2 = float(input(f"Enter the second numbers: "))
if num1 % num2 == 0:
    print(f"Even number")
else:
    print("Odd number")
    
    
num1 = int(input(f"Enter the first numbers: "))
# num2 = int(input(f"Enter the second numbers: "))
for i in range(num1):
    if(i % 2!=0):
        print("Odd Number is: ")
        print(i)
    elif (i%2 == 0):
        print("Even number is: ")
        print(i)
print()

a = 10
for i in range(a):
    print(i)
