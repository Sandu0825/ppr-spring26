import json

# Open and read JSON file
with open("sample-data.json") as file:
    data = json.load(file)
    #Converts JSON file → Python dictionary.

# Print header
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)
#The important keys are: dn,speed ,mtu

# Loop through interfaces
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    #Go inside nested dictionary.
    
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    #Safely gets value. If key doesn't exist → returns empty string.

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))