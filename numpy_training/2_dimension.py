import numpy as np

zero_d_array = (2)
one_d_array = [1,2,3,4]
two_d_array = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
]

convert_to_numpyarray = np.array(two_d_array)

# Check number of dimensions (.ndim)

print(convert_to_numpyarray)
print(f"Number of dimension of the above array is `{convert_to_numpyarray.ndim}`")

#  array စဆောက် ကတည်းက ndmin သုံးပီး dimesion သတ်မှတ်ပေးလို့ရ
# np.array((1,2), ndmin=2)