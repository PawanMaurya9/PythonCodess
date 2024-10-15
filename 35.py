n=int(input("n: "))
for i in range(n):
    # val=1
    for j in range(n):
        if i + j >=n - 1:
            print('*',end=" ")
            # val+=1
        else:
            print(" ",end=" ")
    print()