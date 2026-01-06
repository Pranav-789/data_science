import numpy as np

lst = [1,2,3,4,5]
# print(lst)


arr = np.array([1,2,3,4,5])
# print(arr)

## one dimensional array
one_d_arr = np.array([1,2,3,4,5,6,7,8,9,10])
# print(one_d_arr)


## two dimensional array
two_d_arr = np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]
                    ])
# print(two_d_arr)

## matrix
matrix = np.array([
    [1,2,3,4],
    [6,7,8,9]
])

# print(matrix)


## creating arrays from python lists
arr = np.array(lst)
# print(arr)
# o/p [1 2 3 4 5]

## with default values
# np.zeros(shape)

zeroes_array = np.zeros(3)
# print(zeroes_array)
# o/p: [0. 0. 0.]

## np.ones(shap)

ones_array = np.ones((2,3))
# print(ones_array)
# o/p: [[1. 1. 1.]
#       [1. 1. 1.]]

## initialize array with specific number instead of 0 or 1

# np.full(shape, value)

filled_arr = np.full((2,2), -1)
# print(filled_arr)
# o/p: [[-1 -1]
#       [-1 -1]]



## creating sequences of numbers in numpy

seq_arr = np.arange(1, 10, 2)
# print(seq_arr)
# o/p: [1 3 5 7 9]

## identity matrix 
# np.eye(n)
identity_mat = np.eye(4)
print(identity_mat)

# python 01_importing.py