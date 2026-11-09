import numpy as np


# array slicing

# a=np.arange(1,51)
# a=a.reshape(10,5)
# print(a)

# print(a[0])
# print(a[3,4])
# print(a[2:5])  # this will print from 2 to 5 (index)
# print(a[0:11])
# print(a[:,2])# column 2 print hoga


# array slicing
# print(a[2:5,4])  #2 se 5 tk ki row ke 4 th column


# print(a[: , ]) # all the rows all the cols

# print(a[: 2,3])
# print(a[: 2,3].dtype)






# MATHEMATICAL OPERATIONS

a=np.arange(0,18).reshape((6,3))
b=np.arange(20,38).reshape((6,3))
print(a)
print(b)

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(b.max())

x=np.sum(b,axis = 1) # sum of rows print krega axis is no. of row here it is one
print(x)

 


#  random numbersss

# a=np.random.random(2)
# print(a)

# b=np.random.random((2,2))
# print(b)

# c=np.random.randint(1,10)  # iss range mei random integer
# print(c)

# c=np.random.randint(1,10 , (2,2))  # iss range mei random integer boh iss dimension ki array mei
# print(c)

# c=np.random.randint(1,10 , (3,4,5))  # iss range mei random integer boh iss dimension ki array mei
# print(c)


# randn : negative values will ne generated

# a=np. arange(1,10)
# print(a)
# b=np.random.choice(a)
# print(b)




# NUM CHAR
s1='sneha is my name'
s2='i am indian'

# a=np.char.add(s1,s2)
# print(a)

# np.char.upper(s1)  #upper = capitalize all letter
#  np.char.lower # lower = lower all letter


# b=np.char.split(s1) # jha pr bhi space hoga string mei vha pr uss word ko list ki ek item 
# bna dia
# print(b)

# s3='sneha is my \n name'
# a=np.char.splitlines(s3)  # isme usne jha \n se pehle ek element consider kia h and name 
# # ko dusra
# print(a)

# a=np.char.replace(s1, 'name' ,'sirname')
# print(a)

# print('************good bye************')

# a=np.char.center('good bye',80,'*') # this easier way to write above
# print(a)