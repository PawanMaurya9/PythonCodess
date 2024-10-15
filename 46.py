n=int(input("n: "))
for i in range(n):
    val=ord("D")
    for j in range(n):
        if i + j == n - 1:
            print(chr(val), end=" ")
            val-=1
        elif i + j >=n - 1:
            print(chr(val),end=" ")
            val-=1
        else:
            print(" ",end=" ")
    print()