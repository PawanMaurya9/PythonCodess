n = int(input("n: "))
val= 1
for i in range(n):
    for j in range(n):
        if i % 2 ==0:
            print('*', end=" ")
        else:
            print(val, end=" ")
    print()
    if i % 2!=1:
        val+= 1