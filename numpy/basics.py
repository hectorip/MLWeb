import numpy as np


data = np.array([1, 1, 3, 5, 8, 13])

print(data)

# Statistical data is availabe in the arrays
print(data.mean())
print(data.sum())

matrix = np.array([
    [1, 1, 3, 5, 8, 13],
    [1, 1, 3, 5, 8, 13],
])

print(matrix)

# Transpose
print(matrix.T)

# dot Product
print(matrix.dot(matrix.T))

# Simple multiplication

print(matrix * matrix)
print(matrix * 2)
print(matrix + 10)