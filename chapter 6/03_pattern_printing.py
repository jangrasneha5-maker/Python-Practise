# Write a program to print the following star pattern. 
# * 
# *** 
# ***** for n = 3

# a=int(input("enter the number:"))
# for i in range(1,a+1):
#     print(" "*(a-i),end="") # this is feature of print statement to end it
#     print("*"*(2*i-1),end="")#this prevent this to print new line own its own
#     print("\n")


# Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 
# a=int(input("enter the number:"))
# for i in range (1,a+1):
#     print("*"*i,end="")
#     print("\n")


# Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * * 
n=int(input("enter the number:"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("")