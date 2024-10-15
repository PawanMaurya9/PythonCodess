n = int(input("n: "))
for i in range(n):
    # val = 1
    for j in range(n):
        if i == 0  or j == n-1 :
            print('*', end=" ")
        else:
            print(" ",end=" ")
    print()