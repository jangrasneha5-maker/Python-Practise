import numpy as np

# np.empty((rows,cols),dtype)===this is used for random generation of arrays

# a=np.empty((4,4),dtype=int)
# print(a)

# np.ones/zeros((rows,cols),dtype)===yeh 1/0 print kregaa

# b=np.ones(6)
# print(b)

# c=np.zeros((2,2),dtype=int)
# print(c)



# slicingggggggg
# np.arange(start,end,step) end wala index will be rejectedd


# a=np.arange(1,28)
# print(a)

# b=np.arange(1,5,2)
# print(b)

# arr.reshape(rows,cols)  take care ki yeh matrix bnaega toh keep in mind that ki jitne article
# hone chahiye utne hi ho  for eg, agar yha range 21 tk hoti toh total article in array
# # will be 10 and matrix mei 9 hone chahiey toh value error hogaa
# e=np.arange(2,20,2)
# print(e)
# e=e.reshape((3,3))
# print(e)

# flatten and revven functions
# flatten  will inverse the reshape mtln multid se simgle array bnayegaa
# a.flatten()
# (i) Return copy of original array 
# (ii) If you modify any value of this array value of original array is not affected. 
# (iii) Flatten() is comparatively slower than ravel() as it occupies memory. 
# (iv) Flatten is a method of an ndarray object.

e=np.arange(1,100,2)
print(e)
e=e.reshape((10,5)) 
print (e)

# e=e.flatten()
# print(e)


# a.ravel):
# (i) Return only reference/view of original array 
# (i) If you modify the array you would notice that the value of original array also changes. 
# (iii) Ravel is faster than  flatten as it does not occupy any memory. 
# (iv) Ravel is a library-level function.


# same as flatten baaki diff is mentionedd
