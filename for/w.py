import numpy as np
# a = np.array([1, 2, 3])
# print(a)
# print(type(a))  # vector

# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(b)   # Matrix

# c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(c)   # Tensor

# DATATYPE

d = np.array([1, 2, 3], dtype=float)
print(d)
print(d.dtype)


import numpy as np

# 1. zeros
arr1 = np.zeros((3, 4))
print("zeros:\n", arr1, "\n")

# 2. ones
arr2 = np.ones((2, 3))
print("ones:\n", arr2, "\n")

# 3. empty (values may be random garbage depending on memory)
arr3 = np.empty((2, 3))
print("empty:\n", arr3, "\n")

# 4. full (filled with a value)
arr4 = np.full((3, 3), 7)
print("full:\n", arr4, "\n")

# 5. eye (identity matrix)
arr5 = np.eye(4)
print("eye:\n", arr5, "\n")

# 6. identity
arr6 = np.identity(3)
print("identity:\n", arr6, "\n")

# 7. arange
arr7 = np.arange(0, 10, 2)
print("arange:\n", arr7, "\n")

# 8. linspace
arr8 = np.linspace(1, 5, 6)
print("linspace:\n", arr8, "\n")

# 9. random.random
arr9 = np.random.random((2, 2))
print("random.random:\n", arr9, "\n")

# 10. random.randint
arr10 = np.random.randint(1, 10, (3, 3))
print("random.randint:\n", arr10, "\n")

# 11. zeros_like (shape of arr10)
arr11 = np.zeros_like(arr10)
print("zeros_like:\n", arr11, "\n")

# 12. ones_like (shape of arr10)
arr12 = np.ones_like(arr10)
print("ones_like:\n", arr12, "\n")

# 13. reshape (convert to another shape)
arr13 = np.arange(12).reshape(3, 4)
print("reshape:\n", arr13, "\n")

# 14. diag (diagonal array)
arr14 = np.diag([1, 2, 3, 4])
print("diag:\n", arr14, "\n")
