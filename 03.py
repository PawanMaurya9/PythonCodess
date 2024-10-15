row = int(input("row: "))
col = int(input("col: "))
val = row
if val > 9:
    val = 9
for i in range(row):
    for j in range(col):
        print(val,end=" ")
    print()
    val-=1
    if val < 9:
        val = 9
        # some problem is there in this code