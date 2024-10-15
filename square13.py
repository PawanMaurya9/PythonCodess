n = int(input("n: "))
for i in range(n):
    val= 1
    for j in range(n):
        if i % 2 ==0:
            print('*', end=" ")
        else:
            print(val, end=" ")
            val+= 1
    print()
    # if i % 2!=1: