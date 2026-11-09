# tuple is immutable

# empty tuple
a=()
print(type(a))

# one element tuple
a=(1,)
print(type(a))

# method  tupleee

# a = (1, 7, 2) 
# • a.count (1): a count (1) will return number of times 1 occurs in a. 
# • a.index (1) will return the index of first occurrence of 1 in a. 

a=(1,4,323,234,242,"sneha","shanu")

no=a.count(4) # 4 ek baar aya h 
print(no)
na=a.index(4)
print(na)