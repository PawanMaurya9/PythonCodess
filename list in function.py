li = [1,2,3,4,5,6]
def prime_number(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count == 2
a=tuple(filter(prime_number,li))
print(a)