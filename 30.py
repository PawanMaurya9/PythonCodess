n=int(input("num: "))
for i in range(n):
    val=ord('A')
    for j in range(n):
        if i<=j:
            print(chr(val),end=" ")
            val+=1
        else:
            print(" ",end=" ")
    print()