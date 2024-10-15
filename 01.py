'''try:
    print('Statement  1')
    print(10/0)
    print('Statement  2')

except ZeroDivisionError as msg:
    print('from except block',type(msg))
print('Outside try except block')'''

'''try:
    a = int(input('ENter a: '))
    b = int(input('Enter b: '))
    print(a/b)
    print('hi')
except ZeroDivisionError as m:
    print('from except block',type(m))
except ValueError as v:
    print('from except block',type(v))
print('Outside try block')'''
