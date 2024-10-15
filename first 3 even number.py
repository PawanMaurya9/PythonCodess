# Write a program to print the first 3 even number from the given number
'''n = int(input('Enter the number : '))
for i in range(n+1, n+7):
    if i % 2 == 0:
        print(i,'Even number ')
    else:
        print(i,'Odd number ')'''

# another method
'''num = int(input())
count = 0
num+=1
while count < 3:
    if num % 2 == 0:
        count+=1
        print(num,end=" ")

    num+=1'''