#Statistics is the science of collecting, organizing, analyzing, interpreting, and presenting data.
# sum, average, mean, medium, min, max
import numpy as np

arr = np.array([20,1,2,3,4,4,5,8])
arr_1 = np.array([201,1,2,3,4,])

diff = len(arr) - len(arr_1)

# if not same shpe need to broadcasting | also dynamically with np.pad | np.concatenate([arr,np.zeros(diff)])
# Mathematical Operation
arr_1_padded = np.pad(arr_1,(0,diff),'constant',constant_values=0)
print(f"Sum of two array is {arr+arr_1_padded}")
print(f"Sub of the array is {arr-arr_1_padded}")
print(f"Multiply of the array is {arr*arr_1_padded}")
print(f"Division of the array is {arr%arr_1_padded}")

# Statistical Operations
# finding means 
print(f"Means of all data is {np.mean(arr)}")
# finding median
print(f"Median of all data is {np.median(arr)}")
# finding min, max
print(f"Minimum of the given value is {np.min(arr)} & Maximum of the given value is {np.max(arr)}")
# sum of all values
print(f"Sum of all values is {np.sum(arr)}")
# Standard deviations
print(f"Standard deviation of the array is {np.std(arr)}")