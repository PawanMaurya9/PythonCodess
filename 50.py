n = int(input("n: "))
str = 1
spc = n - 1
for i in range(n):
    for j in range(spc):
        print(" ",end=" ")
    for k in range(str):
        print("*",end=" ")
    print()
    str+=2
    spc-=1