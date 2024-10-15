n=int(input("num: "))
val=ord('Z')
for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(val),end=" ")
        else:
            print(" ",end=" ")
    print()
    val-=1