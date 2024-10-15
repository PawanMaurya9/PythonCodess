n = int(input("n: "))
val = ord("A")
for i in range(n):
    bal1 = n
    bal2 = n
    for j in range(n):
        if i == j:
            print(chr(val), end=" ")
            val+=1
        elif i > j:
            print(bal1, end=" ")
            bal1-= 1
        else:
            print(bal2 , end=" ")
            bal2 -=1
    print()
    # val -= 1