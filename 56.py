n = int(input("n: "))
val = ord("A")
for i in range(n):
    print("  "*(n-i-1)+(chr(val)+" ")*(2*i+1))
    val+=1