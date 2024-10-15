# Write a Python Program to count the frequency of words appearing in a string
#Ex: sheena loves eating apple and mango. Her sister also loves eating apple and mango
def frequency_words():
    str = input("Enter a string: ")
    li = str.split()
    d = {}
    for i in li:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] +1
    print(d)
frequency_words()