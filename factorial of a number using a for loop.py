# Write a Python program to find the factorial of a number using a for loop.
n = int(input("Enter the number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"The factorial of {n} is: {fact}")