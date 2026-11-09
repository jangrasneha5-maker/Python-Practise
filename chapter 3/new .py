import numpy as np

# a = np.array([1, 2, 3, 4, 5])
# print(a)

# print(a.shape) # Output: (5,)
# print(a.ndim)  # Output: 1
# print(a.dtype) # Output: int64 (or int32)
# print(a.size)  # Output: 5

# print(np.zeros((3, 3)))
# print(np.ones((2, 4)))
# print(np.eye(3))

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# a = np.array([1,4,9])

# print(np.sqrt(a))
# print(np.exp(a))
# print(np.log(a))


# a = np.array([10,20,30,40])

# print(np.sum(a))
# print(np.mean(a))
# print(np.max(a))
# print(np.min(a))
# print(np.std(a))

a = np.array([[1,2,3],[4,5,6]])

print(np.sum(a, axis=0))
print(np.sum(a, axis=1))