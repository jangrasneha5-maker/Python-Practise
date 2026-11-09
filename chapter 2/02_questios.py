#  # Write a python program to display a user entered name followed by Good 
# #Afternoon using input () function. 
# name=input("enter your name: ")

# print(f"good afternoon {name}") # here we have used "f string" to print name 



# # Write a program to fill in a letter template given below with name and date. 
# letter = '''Dear <|Name|>, 
# You are selected!
# <|Date|> '''

# print(letter.replace("<|Name|>","Sneha").replace("<|Date|>","27 december 2025"))


#  Write a program to detect double space in a string.
# b="sneha  is a good girl"
# print(b.find("  "))

# Replace the double space from problem 3 with single spaces. 
# b="sneha  is a good girl"
# print(b.replace("  "," "))

# Write a program to format the following letter using escape sequence characters. 
letter = "Dear XYW, this python course is nice. Thanks!"
print(letter)
# formatted code
letterformatted = "Dear XYW,\nthis python course is nice.\nThanks!"
print(letterformatted)