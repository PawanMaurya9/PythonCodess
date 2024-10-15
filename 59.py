n=int(input('n: '))
for i in range(-n + 1, n):
    print('* ' *(n-abs(i)))