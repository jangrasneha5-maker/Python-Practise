# s = open(r"C:\Users\Sneha Jangra\Desktop\COMPUTER LANGUAGE\python\chapter 8\file.txt")
# data = s.read()
# print(data)
# s.close()

#  this same can be done using with statment like this
with open(r"C:\Users\Sneha Jangra\Desktop\COMPUTER LANGUAGE\python\chapter 8\file.txt") as f:
    print(f.read())
   
# yeh f.close() likhne ki jarurat nhi h 