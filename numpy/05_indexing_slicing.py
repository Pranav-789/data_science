import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0]) ## 10
print(arr[2]) ## 30
print(arr[-1]) ## 50


print(arr[1:4:2]) ## slicing start, stop(excluded), steps
## o/p: [20 40]

print(arr[:4])
## o/p: [10 20 30 40]

print(arr[::2])
## o/p: [10 30 50]

print(type(arr))
## o/p: <class 'numpy.ndarray'>

## fancy indexing -> selecting multiple index at ones

print(arr[[0, 4, 2]])

## boolean masking

print(arr[arr>25])

## python 05_indexing_slicing.py