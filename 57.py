n = int(input("n: "))
val = ord("A")
for i in range(n):
    print("  " * i + (chr(val) + " ") * (2 * (n - i) - 1))
    val += 1