str = ['a','b','c','d','f']
def vowel(n):
    a = 'AEIOUaeiou'
    if n in a:
        return True
    return False
a = tuple(filter(vowel,str))
print(a)