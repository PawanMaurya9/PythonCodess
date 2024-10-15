a = int(input("a: "))
b = int(input("b: "))
print(f"before swapping\na: {a}\nb: {b}")
#another method using addition and subtraction method
# a = a + b
# b = a - b
# a = a - b
a = a + b
b = a - b
a = a - b
# another method instead of using temp variable using multiplication and division method
# a = a * b
# b = a // b
# a = a // b
#another method using temp
# c = a
# a = b
# b = c
#another method using XOR OPERATOR
# a = a ^ b
# b = a ^ b
# a = a ^ b
#another method in a single line
#and this method can use for any kinds of data type
# a,b = b,a
print(f"After swapping\na: {a}\nb: {b}")