'''#Step
1) Controlling numbers of rows
2) Controlling numbers of columns
3) Controlling numbers of values'''

row = int(input("row: "))
col = int(input("col: "))
for i in range(row):
    for j in range(col):
        print('#',end=" ")
    print()