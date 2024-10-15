# swap the value using third variables
a = int(input(f"Enter the first number: "))
b = int(input(f"Enter the second number: "))
print(f"before swapping\na: {a}\nb: {b}")
c = a 
a = b
b = c
print(f"After swapping\na: {a}\nb: {b}")