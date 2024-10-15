# write a program to find the second maximum number from the given list
'''a = [2,3,5,3,1,8,4,2]
for i in range(1,len(a)):
    for j in range(1,len(a)):
        if a[j-1] < a[j]:
            a[j-1],a[j] = a[j],a[j-1]
    print(a)
print(a[1])'''
'''a = [2,3,5,3,1,8,4,2]
fmax = 0
smax = 0
for num in a:
    if num>fmax:
        fmax = num
for num in a:
    if num>smax and num<fmax:
        smax = num
print(smax)
'''