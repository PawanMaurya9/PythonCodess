n=int(input("n: "))
val=1
for i in range(n):
    for j in range(n):
        if i<=j:
            print(val,end=" ")
        else:
            print(" ",end=" ")
    print()
    val+=1