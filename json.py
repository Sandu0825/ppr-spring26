#1:
import json
# JSON string
json_string = '{"fruit": "apple", "quantity": 5}'

# Convert JSON to Python dictionary
data = json.loads(json_string)
#json.loads() turns JSON text into a Python dictionary.
#Then get values using the keys.

# Print values
print("Fruit:", data["fruit"])      # Output: apple
print("Quantity:", data["quantity"]) # Output: 5


#2:
import json
# Python dictionary
person = {"name": "Tom", "age": 20}

# Convert to JSON string
json_text = json.dumps(person)

print("JSON:", json_text)  # Output: {"name": "Tom", "age": 20}


#3:write json to a file
import json

# Python data
data = {"city": "Almaty", "country": "Kazakhstan"}

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f)

print("JSON written to data.json")
#
#json.dump() saves Python data as JSON into a file.


#4:read json from a file
import json
# Read JSON from file
with open("data.json", "r") as f:
    data = json.load(f)

# Print data
print(data)
# Output: {'city': 'Almaty', 'country': 'Kazakhstan'}


