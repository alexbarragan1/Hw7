import numpy as np

matrix = np.arange(25).reshape(5, 5)
print("Matrix:")
print(matrix)

alternate_rows = matrix[[0, 2, 4]]
print("\nAlternate Rows:")
print(alternate_rows)