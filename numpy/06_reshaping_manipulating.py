import numpy as np

arr = np.array([1,2,3,4,5,6])

## reshaping the array -> happens when the dimensions match the number of elements
reshaped_arr = arr.reshape(2, 3)
## reshaping does not create a copy
## returns a view affecting the array


print(reshaped_arr)

## flattenning the array (multi-demensional -> 1D)


## .ravel() -> view
## .flatten() -> copy

arr_2d = np.array([[1,2,3], [4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())

## python 06_reshaping_manipulating.py