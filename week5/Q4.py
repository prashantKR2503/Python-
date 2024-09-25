def merge_odd_even(list1,list2):
    odd_l = [x for x in list1 if x%2 != 0]
    even_l = [x for x in list2 if x%2 == 0]
    return odd_l + even_l
    
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = merge_odd_even(list1, list2)
print("Merged List:", result)