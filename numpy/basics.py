import numpy as np

# Declaración de Array
data = np.array([1, 1, 3, 5, 8, 13])

print(data)

# Los datos estadísiticos están disponibles como
# funciones de arrays
print(data.mean())
print(data.sum())
print(data.var())
print(data.std())

matrix = np.array([
    [1, 1, 3, 5, 8, 13],
    [1, 1, 3, 5, 8, 13],
])
print(matrix)

f_array = np.array([1, 5, 6, 7, 7], float)
print(f_array)

# Transpuesta
print(matrix.T)

# Producto punto
print(matrix.dot(matrix.T))

# Operaciones simples

print(matrix * matrix)
print(matrix * 2)
print(matrix + 10)
print(matrix - 10)
print(matrix / 2)