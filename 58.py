n = int(input("n: "))
val = ord("A")

# Print the initial pyramid
for i in range(n):
    print("  " * (n - i - 1) + (chr(val) + " ") * (2 * i + 1))
    val += 1

# Reset val for the reverse pyramid
val -= 1

# Print the reverse pyramid
for i in range(n):
    print("  " * i + (chr(val) + " ") * (2 * (n - i) - 1))
    val -= 1