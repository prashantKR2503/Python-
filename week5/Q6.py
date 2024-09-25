import numpy as np

arr = np.array([[9,5,1],
                [4,8,2],
                [0,3,6]
                ])
print("Original Numpy array\n",arr)

arrSortByRow = arr[:,arr[1,:].argsort()]
print("Sort array by the second row\n",arrSortByRow)

arrSortByColumn = arr[arr[:,1].argsort(),:]
print("Sort array by the second column\n",arrSortByColumn)
