row = int(input("row: "))
col = int(input("col: "))
val = 1
for i in range(row):
    for j in range(col):
        print(val,end=" ")
    print()
    val+=1