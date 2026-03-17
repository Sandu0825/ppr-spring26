# This program shows enumerate() and zip()
names = ["Dana", "Nazerke", "Zamira"]
scores = [85, 90, 78]
#enumerate() gives index + value
print("Using enumerate:")
for index, name in enumerate(names):
    print(index, name)

#zip() combines two lists element by element
print("\nUsing zip:")
for name, score in zip(names, scores):
    print(name, score)

#using sorted()
numbers = [5, 1, 9, 3]
sorted_numbers = sorted(numbers)

print("\nSorted numbers:", sorted_numbers)

#type conversion examples
a = "10"
b = "20"
#convert strings to integers
sum_numbers = int(a) + int(b)
print("Converted sum:", sum_numbers)