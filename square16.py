n = int(input("n: "))
for i in range(n):
    val = 1
    for j in range(n):
        if i ==j :
            print('*', end=" ")
        elif i > j:
            print(val, end=" ")
            val+= 1
        else:
            print(val,end=" ")
            val+= 1

    print()
    if val > 9:
        val = 1