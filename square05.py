'''row = int(input("row: "))
col = int(input("col: "))
for i in range(row):
    val = 1
    for j in range(col):
        print(val,end=" ")
        val+=1
    print()'''

for a in range(1,10):
    for b in range(1,a+1):
        print("*",end=" ")
    print()