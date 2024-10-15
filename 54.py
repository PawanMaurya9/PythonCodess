n = int(input("n: "))
val = 1
for i in range(n):
    for j in range(n-1-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()