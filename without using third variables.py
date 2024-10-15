# without using third variables
a = int(input(f"Enter the first number: "))
b = int(input(f"Enter the second number: "))
print(f"before swapping\na: {a}\nb: {b}")
a = a + b
b = a - b
a = a - b
print(f"After swapping\na: {a}\nb: {b}")