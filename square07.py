row = int(input("row: "))
col = int(input("col: "))
val = ord('A')
for i in range(row):
    for i in range(col):
        print(chr(val), end=" ")
    print()
    val+=1
    if val > ord("Z"):
        val = ord("A")