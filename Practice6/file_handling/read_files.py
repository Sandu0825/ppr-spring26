#this program shows different ways to read a file

# open file in read mode
file = open("sample.txt", "r")

# read the whole file as one string
content = file.read()
print("Using read():")
print(content)
file.close()


#read file line by line using readline()
file = open("sample.txt", "r")

print("\nUsing readline():")
line1 = file.readline()   #reads first line
line2 = file.readline()   #reads second line
print(line1)
print(line2)
file.close()


#read all lines into a list
file = open("sample.txt", "r")

print("\nUsing readlines():")
lines = file.readlines()   #each line becomes an element in the list
print(lines)
file.close()