# Write a Python Program to convert two lits into the dictionary
# eg:
# list1 = [Naina, Kimi, sheena]
# kist2 = [852345, 763567, 691276]

def list_to_dic():
    keys= [1,2,3]
    values = ["one", "two", "three"]
    result = dict(zip(keys, values))
    print(result)
list_to_dic()

def list_to_dic():
    keys = ["Naina", "Kimi", "sheena"]
    values = [852345, 763567, 691276]
    result = dict(zip(keys, values))
    print(result)
list_to_dic()