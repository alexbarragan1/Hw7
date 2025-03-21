import numpy as np

matrix = np.random.randint(1, 100, size=(10, 10))
print("Matrix:")
print(matrix)

sorted_matrix = matrix[matrix[:, 0].argsort()]
print("\nSorted Matrix:")
print(sorted_matrix)