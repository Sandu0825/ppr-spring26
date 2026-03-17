# This program moves files between folders
import shutil
import os
#create directories
os.makedirs("folderA")
os.makedirs("folderB")

#create a test file
#creates file test.txt inside folderA
with open("folderA/test.txt", "w") as f:
    f.write("This file will be moved")

#move the file to another directory
#takes file from folderA moves it to folderB
shutil.move("folderA/test.txt", "folderB/test.txt")

print("File moved from folderA to folderB")