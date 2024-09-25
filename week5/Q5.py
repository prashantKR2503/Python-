import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print(arr)
odd_rows_even_columns = arr[1::2,0::2] 
print("Array Odd rows and even columns:\n", odd_rows_even_columns)
