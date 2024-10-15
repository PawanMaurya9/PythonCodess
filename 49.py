n = int(input("n: "))
val= ord("A")
for i in range(n):
    for j in range(n):
        if i + j == n -1:
            print(chr(val), end=" ")
        else:
            print(" ",end=" ")
    print()
    val+=1 