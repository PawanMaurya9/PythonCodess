n = int(input("n: "))
for i in range(n):
    val = n
    for j in range(n):
        if i <= j:
            print(val, end=' ')
            val -= 1
        else:
            print(" ", end=' ')
    print()