list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

#Reverse the list
reversed_List = list(reversed(list2))


# Iterating over both lists simultaneously
for num, letter in zip(list1, reversed_List):
    print(f"{num} - {letter}")