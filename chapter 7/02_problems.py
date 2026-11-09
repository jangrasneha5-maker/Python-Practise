#  Write a program using functions to find greatest of three numbers.


# def greatest(a,b,c):
#     if(a>b and a>c):
#         return f"{a}is the greatest"
#     elif(b>a and b>c):
#         return f"{b} is greatest"
#     else:
#         return f"{c} is greatest"

# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# c=int(input("enter the value of c:"))

# print(greatest(a,b,c))




# Write a python program using function to convert Celsius to Fahrenheit. 
# def convert(a):
#     F = (a*(9/5)) + 32
#     return F
# a=int(input("enter the c value: "))
# print(f"the same shit in f is {convert(a)}")   


# Write a recursive function to calculate the sum of first n natural numbers. 
# def sum(s):
#     if(s==1):
#         return 1
#     else:
#         return s+sum(s-1)
    
# num=int(input("enter the number:"))

# result=sum(num)
# print(result)


# Write a python function to remove a given word from a list ad strip it at the same time.
# remove  ke liye
def rem(l,word):
    for item in l:
        l.remove(word)
        return l
    
l=["sneha","suhani","meena"]
print(rem(l,"meena"))

# strip ke liye
def strip(l,word):
    
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
        return n
l=["sneha","suhani","meena"]
print(strip(l,"a"))



# 8. Write a python function to print multiplication table of a given number. 
# def table(n):
#     for i in range(1,11):
#         print(f"{n}x{i}={n*i}")

# n=int(input("enter the number :"))
# print(f"{table(n)}")