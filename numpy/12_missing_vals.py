import numpy as np

# --------------------------------------------------
# Handling NaN (Not a Number) values
# --------------------------------------------------

# Create array with NaN values
arr = np.array([1, 2, np.nan, 4, np.nan, 6])

# np.isnan() returns True for NaN, False otherwise
print(np.isnan(arr))

# NaN cannot be compared directly
# print(np.nan == np.nan)  # always False

# Replace NaN with a fixed value (default = 0)
cleaned_nan_arr = np.nan_to_num(arr, nan=0)
print(cleaned_nan_arr)


# --------------------------------------------------
# Handling Infinity values
# --------------------------------------------------

# Create array with positive and negative infinity
arr_inf = np.array([1, 2, np.inf, 4, -np.inf, 6])

# np.isinf() checks for both +inf and -inf
print(np.isinf(arr_inf))

# Replace +inf and -inf with custom values
cleaned_inf_arr = np.nan_to_num(
    arr_inf,
    posinf=1000,
    neginf=-1000
)
print(cleaned_inf_arr)

# File: 12_missing_vals.py
