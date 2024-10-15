n = int(input("n: "))
for i in range(n):
    val = ord("A") + n - 1
    for j in range(n):
        if i>=j:
            print(chr(val),end=' ')
            val-=1
        else:
            print("",end=' ')
    print()