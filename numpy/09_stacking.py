import numpy as np

# Create two 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Vertical stacking → converts 1D arrays into rows
# Result shape: (2, 3)
print(np.vstack((arr1, arr2)))

# Horizontal stacking → joins arrays side by side
# Result shape: (6,)
print(np.hstack((arr1, arr2)))


# Create a 1D array for splitting
arr_to_split = np.array([10, 20, 30, 40, 50, 60])

# Split the array into 2 equal parts
# Returns a list of NumPy arrays
print(np.split(arr_to_split, 2))


## python 09_stacking.py