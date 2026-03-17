#this program copies and deletes files
import shutil
import os
#os = control files and folders
#shutil is for moving, copying, organizing files

# copy a file
# sample.txt will be copied to backup.txt
shutil.copy("sample.txt", "backup.txt")
print("File copied")

# check if file exists before deleting
if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("Backup file deleted")
else:
    print("File does not exist")