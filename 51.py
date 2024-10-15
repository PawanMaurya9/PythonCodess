n = int(input("n: "))
str = 1
spc = n - 1
for i in range(n):
    print(" "*spc+"* "*str)
    str+=2
    spc-=1