import numpy as np

arr_2d = np.array([
    [1,2,3],
    [4,5,6]
])


## get dimensions of array
print(arr_2d.shape)
# o/p (2, 3)


## get size of array (number of elements)
print(arr_2d.size) # o/p: 6

## get number of dimensions of array
print(arr_2d.ndim) # o/p: 2

## get data type of element
print(arr_2d.dtype) # o/p: int64

## python 02_properties.py