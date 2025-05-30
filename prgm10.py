import numpy as np
#initial array
arr = np.array([[-1,2,0,4],
              [4,-0.5,6,0],
              [2.6,0,7,8],
              [3,-7,4,2.0]])
print("intial array:")
print(arr)
#printing a range of array
#with the use of slicing method
sliced_arr=arr[:2,::2]
print("array with first 2 rows and"
      "alternate columns(0 and 2):\n",
      sliced_arr)
#printing elements at
#specaial indices
index_arr = arr[[1, 3], [3, 0]]
print("\nElements at indices(1,3),"
      "(3,0):\n",index_arr)
