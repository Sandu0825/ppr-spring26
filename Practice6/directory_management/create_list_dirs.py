# This program works with directories (folders)
import os

#create a new folder
os.mkdir("my_folder")

#create nested folders
os.makedirs("parent/child/grandchild")
print("Directories created")

#show current working directory
print("Current directory:", os.getcwd())


#list all files and folders in current directory
items = os.listdir()
print("Files and folders here:")
for item in items:
    print(item)

#remove an empty directory
os.rmdir("my_folder")
print("my_folder removed")