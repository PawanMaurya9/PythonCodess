def num(*n):
    sum = 0
    for i in n:
        sum+=i
    return sum
c = num(1,2,3,4,5,6)
print(c)