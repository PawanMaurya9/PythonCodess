n=int(input("n: "))
for i in range(n):
    val=4
    for j in range(n):
        if i + j <=n - 1:
            print(val,end=" ")
            val-=1
        else:
            print(" ",end=" ")
    print()