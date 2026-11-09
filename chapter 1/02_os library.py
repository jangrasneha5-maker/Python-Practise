import os

# Specify the directory you want to list
# '.' means the current directory where this file is located
directory_path = '.' 

# Get the list of all files and directories
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)