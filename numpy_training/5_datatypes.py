import numpy as np


# interger = i
# boolean = b
# unsigned integer = u
# float = float
# complex = c
# String = S
# UnicodeString = U
# timedelta = m etc.
arr = np.array([1,2,3,4,5,6,"a"])
string_array = np.array(["a","b","c","d"])

# .dtype method ကိုသုံးပီး data type ကိုသိလို့ရ

print(f"Given array's data type is {string_array.dtype}")


# array  လုပ်ကတည်းက data type တန်းပြောလို့ရ

string_array_defind = np.array([1,2,3,4,5,6], dtype='S')

print(f"\nThis datatype is the predefined as the String 's' at the intial state {string_array_defind} ")


# astype ကိုသုံးပီး existing datatype ကို comvert လုပ်လို့ရတယ်

float_datatype_array = np.array([1.1,2.2,3.3])

inter_changed = float_datatype_array.astype('i')

print(f"This is the before state integer changed {float_datatype_array}")
print(f"This is the after state integer changed {inter_changed}")
