import re      #module for working with regular expressions
import json    #module for creating JSON output

#1."r" means read mode
# encoding="utf-8" allows correct reading of text
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()   # Save full file content into variable "text"


#2.Find product names and their prices together
# ([A-Za-z ]+) - product name (letters and spaces)
# \s+ -one or more spaces
# (\d+\.\d{2}) - price like 2.50 or 15.99
# re.findall() returns a list of tuples:product, price
items = re.findall(r"([A-Za-z ]+)\s+(\d+\.\d{2})", text)

#empty lists to store results
products = []
prices = []

#Loop through each found item
for name, price in items:
    products.append(name)        # add product name to list
    prices.append(float(price))  # convert price from string to float


#3.Calculate total price
#round(.,2) keeps 2 decimal places
total = round(sum(prices), 2)


#4.Extract date and time
#Format YYYY-MM-DD HH:MM
date_match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", text)

#If date is found -take matched value
#If not → return "Not found"
date_time = date_match.group() if date_match else "Not found"


#5.Extract payment method
#Looks for Payment Method: CASH or VISA
#(\w+) captures the payment word
payment_match = re.search(r"Payment Method: (\w+)", text)

payment_method = payment_match.group(1) if payment_match else "Not found"


#6.Create structured dictionary (like JSON object)
receipt = {
    "products": products,
    "prices": prices,
    "total": total,
    "date_time": date_time,
    "payment_method": payment_method
}


#7. Convert dictionary to formatted JSON and print
# indent=4 makes output readable
print(json.dumps(receipt, indent=4))