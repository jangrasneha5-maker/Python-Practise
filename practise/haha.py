# # Create a NumPy array with values: 5, 10, 15, 20.Print its type

# import numpy as np
# # a=np.array([5,10,15,20])
# # print(type(a))

# # a = np.array([1, 2, 3]). Add 5 to each element.Multiply each element by 2

# # a=np.array([1,2,3])
# # new_a=(a+5)*2
# # print(new_a)

# # Zeros and Ones.Create a 3×3 matrix of zeros.Create a 2×4 matrix of ones

# # b=np.ones((2,4))
# # print(b)

# # c=np.zeros((3,3))
# # print(c)

# # Create an array from 1 to 20 with step size 2

# # a=np.arange(1,21,2)
# # print(a)

# # a = np.array([10, 20, 30, 40, 50]).Print 2nd and 4th element.Slice elements from index 1 to 3

# # a = np.array([10, 20, 30, 40, 50])
# # print(a[2])
# # print(a[4])

# # a_new=a[1:4]
# # print(a_new)

# # Create array from 1 to 12.Convert it into a 3×4 matrix

# a=np.array(1,13)
# print(a)

# a=np.arange(1,13,1)
# print(a)




# def cal(a,b,op='+'):
#     if(op=='+'):
#         return (a+b)
#     if(op=='-'):
#         return (a-b)
#     if(op=='*'):
#         return (a*b)
#     if(op=='/'):
#         return (a/b)
#     else:
#         return ("invalid input")
    
# a=int(input("Enter your no. :"))
# b=int(input("Enter your no. :"))

# print(cal(a,b,'-'))


# def sum_all(*args):
#     total=0
#     for num in args:
#         if num>0:
#             total += num
#     return total
    
# print(sum_all(10,-5,20,30))


# def sum_digits(n):
#     if n==0:
#         return 0
#     return (n % 10) +sum_digits(n//10)

# print(sum_digits(1234))

# def reverse(s):
#     if len(s)==0:
#         return s
#     else:
#         return reverse(s[1:])+s[0]
    
# print(reverse("akhil"))

# search_word="python"
# replace_word="c++"
# file_path=r"C:\Users\Sneha Jangra\Desktop\COMPUTER LANGUAGE\python\practise\project.txt"
# with open(file_path,"r") as f:
#     data=f.read()

# new_data=data.replace(search_word,replace_word)

# with open(file_path,"w") as f:
#     f.write(new_data)

# Part 1: Writing
# emp_data=r"C:\Users\Sneha Jangra\Desktop\COMPUTER LANGUAGE\python\practise\emp_data.txt"
# n = int(input("How many employees? "))
# with open(emp_data, "a") as f:
#     for i in range(n):
#         name = input("Name: ")
#         eid = input("ID: ")
#         sal = input("Salary: ")
#         f.write(f"{name} | {eid} | {sal}\n")

# # Part 2: Reading & Calculating
# total_sal = 0
# with open(emp_data, "r") as f:
#     for line in f:
#         parts = line.split("|")
#         total_sal += float(parts[2].strip())

# print(f"Total Expenditure on Salaries: {total_sal}")



# import numpy as np

# A=np.array([[1,2,3],[4,5,6],[7,8,9]])
# B=np.array([[9,8,7],[6,5,4],[3,2,1]])

# add_res=A+B
# dot_res=np.dot(A,B)
# print(dot_res) 

# import numpy as np

# arr = np.random.randint(1, 101, 20)

# print(f"Mean: {np.mean(arr)}, Median: {np.median(arr)}")

# # Boolean Indexing (Very important for exams!)
# arr[arr > 50] = 0
# print("Modified Array:", arr)


# import pandas as pd

# data = {
#     'Name': ['Sneha', 'Rahul', 'Amit', 'Priya'],
#     'Marks': [85, 32, 78, 90]
# }

# df = pd.DataFrame(data)

# # Adding a column using a lambda or conditional logic
# df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')

# # Filtering
# passed_students = df[df['Result'] == 'Pass']
# print(passed_students)



import pandas as pd
import numpy as np

df = pd.DataFrame({'Emp': ['A', 'B', 'C'], 'Salary': [5000, np.nan, 7000]})

# 1. Check for nulls
print(df.isnull().sum())

# 2. Fill with mean
mean_sal = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(mean_sal)


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 40]

plt.plot(x, y, color='blue', marker='o')
plt.title("Growth Chart")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()



try:
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    print("Result:", a / b)
except ValueError:
    print("Input numbers only, please!")
except ZeroDivisionError:
    print("Zero se divide mat karo!")