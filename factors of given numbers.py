#write a program to print the factors of given numbers
x = int(input("Enter the first number: "))
for i in range(1,x+1):
    if x % i == 0:
        print(i)