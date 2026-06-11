import numpy as np

arr_int = np.array([10, 20, 30], dtype=int)
arr_float = np.array([1.5, 2.5, 3.5], dtype=float)
arr_bool = np.array([True, False, True], dtype=bool)

print("Integer dtype:", arr_int.dtype)
print("Float dtype:", arr_float.dtype)
print("Boolean dtype:", arr_bool.dtype)

arr_float2 = arr_int.astype(float)

print("Converted to Float:", arr_float2)

print("Shape:", arr_int.shape)
print("Size:", arr_int.size)
 
 
 
 
