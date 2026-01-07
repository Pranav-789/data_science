import numpy as np

prices = np.array([100, 200, 300])

discount = 10

final_prices = prices - (prices*discount/100)

print(final_prices)
# o/p: [200 400 600]

# single value
arr = np.array([100, 200, 300])
print(arr*2)
# o/p: [ 90. 180. 270.]

## 1D to 2D broadcasting

matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([10, 20, 30])

result = matrix + vector
print(result)

## o/p: [[11 22 33]
#       [14 25 36]]


## error for incompatible shape

arr1 = np.array([[1,2,3],[4,5,6]]) ## shape(2,3)
arr2 = np.array([1,2]) ## shape 2

print(arr1 + arr2)
## ValueError: operands could not be broadcast together with shapes (2,3) (2,) 

## python 10_broadcasting.py