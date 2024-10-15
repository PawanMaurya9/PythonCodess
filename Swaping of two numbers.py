'''a = int(input('a: '))
b = int(input('b: '))
print(f"before awaping\n a:{a}\n b:{b}")
# c = a
# a = b
# b = c

# without using third variables 
a = a + b
b = a - b
a = a - b
print(f"After swaping\n a:{a}\n b:{b}")'''

#Swapping of two variable without using temp variable 
a = int(input(f"Enter the first number: "))
b = int(input(f"Enter the second number: "))
print(f"Before Swapping\n a: {a}\n b: {b}")
a,b=b,a
print(f"After Swapping\n a: {a}\n b: {b}")