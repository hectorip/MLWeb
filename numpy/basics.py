import numpy as np


data = np.array([1, 1, 3, 5, 8, 13])

print(data)
print(data.mean())
print(data.sum())

matrix = np.array([
    [1, 1, 3, 5, 8, 13],
    [1, 1, 3, 5, 8, 13],
])

print(matrix)
print(matrix.T)

print(matrix.dot(matrix.T))

# Simple multiplication

print(matrix * matrix)
print(matrix * 2)