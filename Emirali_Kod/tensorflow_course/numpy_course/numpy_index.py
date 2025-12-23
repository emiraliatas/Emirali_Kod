import numpy as np

other_array = np.arange(0,24)
slicing_array = other_array[4:9]
print(slicing_array)
slicing_array[:] = 700
print(slicing_array)
print(other_array)

ex_array = np.arange(0,24)
ex_array_copy = ex_array.copy()

ex_array_copy_slicing = ex_array_copy[2:9]
print(ex_array_copy_slicing)
ex_array_copy_slicing[:] = 200
print(ex_array_copy_slicing)
print(ex_array_copy)
print(ex_array)