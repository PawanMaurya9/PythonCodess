n = int(input("n: "))
val = 1
for i in range(n):
    print("  "*(n-i-1)+(str(val)+" ")*(2*i+1))
    val+=1