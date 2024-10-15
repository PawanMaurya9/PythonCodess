n = int(input("n: "))
val = ord("1") + n - 1
for i in range(n):
    
    for j in range(n):
        if i==j:
            print(chr(val),end=' ')
        else:
            print(" ",end=' ')
    print()
    val-=1