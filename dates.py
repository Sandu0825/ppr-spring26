#timedelta is a class from the datetime module that represents a duration of time — not a date, 
#not a clock time — just a time difference.

#1:
from datetime import datetime, timedelta

# Get current date and time
current_date = datetime.now()

# Create a time difference of 5 days
five_days = timedelta(days=5)

# Subtract 5 days from current date
new_date = current_date - five_days

# Print result
print("Current date:", current_date)
print("Date before 5 days:", new_date)


#2:
from datetime import datetime, timedelta

# Get today's date
today = datetime.now()

# Calculate yesterday (subtract 1 day)
yesterday = today - timedelta(days=1)

# Calculate tomorrow (add 1 day)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#3:
from datetime import datetime

# Get current date and time
now = datetime.now()

# Remove microseconds
no_microseconds = now.replace(microsecond=0)

print("With microseconds:", now)
print("Without microseconds:", no_microseconds)


#4:
from datetime import datetime

# Create two dates (year, month, day, hour, minute, second)
date1 = datetime(2026, 2, 20, 10, 0, 0)
date2 = datetime(2026, 2, 24, 10, 0, 0)

# Subtract dates
difference = date2 - date1

# Convert difference to seconds
seconds = difference.total_seconds()
#total_seconds() converts that time difference into seconds.

print("Difference in seconds:", seconds)