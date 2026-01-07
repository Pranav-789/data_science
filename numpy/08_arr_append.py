import numpy as np

# =====================================================
# 1️⃣ ONE-DIMENSIONAL (1D) ARRAY EXAMPLES
# =====================================================

# Create a 1D NumPy array
original_array = np.array([10, 20, 30])

# np.append DOES NOT modify the original array
# It returns a NEW array (COPY) with extra elements added
appended_array = np.append(original_array, [40, 50, 60])

print("Original array:", original_array)
print("Appended array:", appended_array)

# Output:
# Original array: [10 20 30]
# Appended array: [10 20 30 40 50 60]

# 👉 Memory behavior:
# original_array  -> unchanged
# appended_array  -> COPY (new memory)


# -----------------------------------------------------
# Concatenating 1D arrays
# -----------------------------------------------------

# axis=0 for 1D arrays means simple extension
concatenated_array = np.concatenate(
    (original_array, appended_array),
    axis=0
)

print("Concatenated array:", concatenated_array)

# Output:
# Concatenated array: [10 20 30 10 20 30 40 50 60]

# 👉 Memory behavior:
# np.concatenate ALWAYS returns a COPY


# -----------------------------------------------------
# Deleting elements from a 1D array
# -----------------------------------------------------

# Remove element at index 0
deleted_array = np.delete(original_array, 0)

print("Array after deletion:", deleted_array)

# Output:
# Array after deletion: [20 30]

# 👉 Memory behavior:
# np.delete returns a COPY
# original_array remains unchanged


# =====================================================
# 2️⃣ TWO-DIMENSIONAL (2D) ARRAY EXAMPLES
# =====================================================

# Create two 2D arrays
array_2d_first = np.array([
    [1, 2],
    [3, 4]
])

array_2d_second = np.array([
    [5, 6],
    [7, 8]
])

print("\nFirst 2D array:\n", array_2d_first)
print("Second 2D array:\n", array_2d_second)

# Output:
# First 2D array:
# [[1 2]
#  [3 4]]
#
# Second 2D array:
# [[5 6]
#  [7 8]]


# -----------------------------------------------------
# Vertical stacking (axis = 0)
# -----------------------------------------------------

vertical_concatenation = np.concatenate(
    (array_2d_first, array_2d_second),
    axis=0
)

print("\nVertical concatenation (axis=0):\n", vertical_concatenation)

# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# 👉 Rows are added
# 👉 Shape changes from (2, 2) → (4, 2)
# 👉 COPY is created


# -----------------------------------------------------
# Horizontal stacking (axis = 1)
# -----------------------------------------------------

horizontal_concatenation = np.concatenate(
    (array_2d_first, array_2d_second),
    axis=1
)

print("\nHorizontal concatenation (axis=1):\n", horizontal_concatenation)

# Output:
# [[1 2 5 6]
#  [3 4 7 8]]

# 👉 Columns are added
# 👉 Shape changes from (2, 2) → (2, 4)
# 👉 COPY is created


# -----------------------------------------------------
# Deleting rows and columns in 2D arrays
# -----------------------------------------------------

# Delete first row (axis=0)
row_deleted_array = np.delete(array_2d_first, 0, axis=0)

print("\nAfter deleting first row:\n", row_deleted_array)

# Output:
# [[3 4]]

# 👉 COPY is created


# Delete first column (axis=1)
column_deleted_array = np.delete(array_2d_first, 0, axis=1)

print("\nAfter deleting first column:\n", column_deleted_array)

# Output:
# [[2]
#  [4]]

# 👉 COPY is created


# =====================================================
# 🔴 FINAL MEMORY SUMMARY (IMPORTANT)
# =====================================================

# Any NumPy operation that CHANGES ARRAY SIZE
# (append, delete, concatenate)
# -----------------------------
# ❌ Cannot be a view
# ✅ ALWAYS creates a COPY
#
# NumPy arrays have FIXED size in memory.
