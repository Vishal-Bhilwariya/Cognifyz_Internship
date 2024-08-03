"""Task: Automate a Task
Identify a repetitive task, such as data processing, file management, or report generation, 
and develop a script to automate it using Python. This task will showcase their problem-solving 
skills and familiarity with Python's automation capabilities."""

print("________________________________________________________")
import os

# creating a DATA name folder and 40 folder inside it using os module
os.mkdir("DATA")
for i in range(1,40):
    os.mkdir(f"DATA/Day{i}")

# note -> if 'DATA' folder already exists then it will through an error .
# please ensure this if present then u can comment above 3 code of lines or 
# delete the existing folder

# providing the folder path
folder_path = 'DATA'

# providing prefix name to be renamed in all file
prefix = '_'

# list all files in the folder
files = os.listdir(folder_path)

# renaming folder name by adding prefix
print("PREVIOUS AND RENAMED FILE NAMES")
i = 1
for file in files:
    # build  the new file name with prefix
    new_name = prefix + file
    
    # Rename the file using os module and function rename()
    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
    
    print(i,") Previous file name =>",file ," : Current file name =>", new_name)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    i += 1

print("-------------------------------")
print('All files renamed successfully!')
print("-------------------------------")

print("________________________________________________________")