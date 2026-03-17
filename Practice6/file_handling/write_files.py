# write_files.py

# "w" mode creates file or overwrites it
with open("sample.txt", "w") as file:
    file.write("Python is easy to learn\n")
    file.write("File handling is useful\n")

# "a" mode adds new content without deleting old content
with open("sample.txt", "a") as file:
    file.write("This line was added later\n")

# read file to check result
with open("sample.txt", "r") as file:
    print("File content:\n")
    print(file.read())