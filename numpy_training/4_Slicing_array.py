import numpy as np

# syntax => [start:end:step] end က exclude

arr = np.array([1,2,3,4,5,6,7,8])

print(f"Slicing from index 1 to index 3 {arr[1:4]}")

# Also negative slicing from the end 
arr_1 = np.array([1,2,3,4,5])
print(f"Slicing negatively {arr_1[-4:-1]}")
