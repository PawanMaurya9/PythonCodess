# Write a program to find the duplicate in the given string
'''a = input('Enter the element: ')
b = ''
dup = ''
for i in a:
    if i not  in b:
        b+=i
    else:
        if i not in dup:
            dup+=i
print(dup)'''
# another way
'''n = input('Enter the string: ')
s=''
for i in n:
    c = 0
    for j in n:
        if j not in s:
            if i == j:
                c+=1
    if c > 1:
        s+=i
        print(s)
        '''
        
# a = 'pyspiders hebbal'
# print(a[0:5:1])
# print(a[3:8:])
# print(a[4:1:-1])
# print(a[10:2:-1])
# print(a[10:-1:-1])
# a = 'python is great'
# print(a[2:11:1])
# print(a[:13:2])
# print(a[::1])
# print(a[0::])
# print(a[12:1:-3])
# print(a[1:0:2])
# b = ['cat','rat','dog','bat']
# print(b[3:1:])
# print(b[1:4:2])
# print(b[0::2])
# print(b[4:0:-1])
# print(b[3:0:-2])
# c = (1,2,3,4,'a')
# print(c[1:4:2])
# print(c[2:4:])
#type casting
#Integer
# a = 10
# print(float(a))
# print(complex(a))
# print(bool(a))
# print(str(a))
#Float
# a = 10.0
# print(int(a))
# print(complex(a))
# print(bool(a))
# print(str(a))
#Complex
# a = 10+1j
# print(bool(a))
# print(str(a))
#Boolean
# a = True
# print(float(a))
# print(complex(a))
# print(int(a))
# print(str(a))
# print(len(str(input('Enter your name: '))))
# from time import *

# print('before sleep') 
# sleep(10)
# print('after sleep')

# from operator import *

# print(add(10,3))
# print(sub(5,2))
# print(mul(3,6))
# print(mod(20,2))
# print(divmod(10,2))
# print(floordiv(20,4))
# print(pow(2,3))


'''x = int(input('Entet the number: '))
for i in range(1,x+1):
    if x%i==0:
        print(i)'''
'''n = int(input('Enter the number: '))
sum = 0
for i in range(1,n+1):
    sum=sum+i
print(sum)'''
'''n = int(input('Enter the number: '))
a = 1
for i in range(a):
    print(f"Natural no. of first four no",n*n-1)'''
'''a=int(input('Enter the number: '))

sum=0
temp=a
c=len(str(a))
while a>0:
    rem=a%10
    sum=sum+rem**c
    a=a//10
if temp==sum:
        print('armstrong')
else:
        print('not armstrong')'''

'''n = int(input('Enter the number: '))
temp = n
sum = 0
while n!=0:
    rem = n%10
    f = 1
    for i in range(1,rem+1):
        f=f*i
    sum =sum+f
    n//=10
if sum ==temp:
    print('Strong number')
else:
    print('Not Strong number')'''































