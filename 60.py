n = int(input('n: '))

# Print the top part of the pattern
for i in range(1, n+1):
    print('  ' * (n - i) + '* ' * i)

# Print the bottom part of the pattern
for i in range(n-1, 0, -1):
    print('  ' * (n - i) + '* ' * i)