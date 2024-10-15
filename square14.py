n = int(input("n: "))
for i in range(n):
    val= 1
    for j in range(n):
        if i ==j :
            print('*', end=" ")
        elif i > j:
            print('$', end=" ")
        else:
            print('#',end=" ")

    print()