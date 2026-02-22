#1:
from datetime import datetime, date

# Create a date object for today
today = date.today()
print("Today's date:", today)  # Example output: 2026-02-22

# Create a specific date: year, month, day
birthday = date(2000, 5, 15)
print("Birthday:", birthday)  # Output: 2000-05-15

# Create a datetime object for now (includes time)
now = datetime.now()
print("Current date and time:", now) # Example: 2026-02-22 15:30:45
#datetime.now() gives both date and time.


#2:
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Default format (standard datetime output)
print("Default format:", now)

# Format date as Year-Month-Day
print("Year-Month-Day:", now.strftime("%Y-%m-%d"))  # e.g., 2026-02-22

# Format date as Day/Month/Year
print("Day/Month/Year:", now.strftime("%d/%m/%Y"))  # e.g., 22/02/2026

# Format date with full weekday and month names
print("Full weekday and month name:", now.strftime("%A, %B %d, %Y"))  
# Example: Sunday, February 22, 2026


#3:
from datetime import datetime, timedelta

# Define two datetime objects
start = datetime(2026, 2, 20, 14, 0)  # Feb 20, 2026 at 14:00
end = datetime(2026, 2, 22, 18, 30)   # Feb 22, 2026 at 18:30

# Subtract the two dates to get a timedelta object
difference = end - start
print("Time difference:", difference)  # Output: 2 days, 4:30:00

# Access number of full days
print("Days:", difference.days)  # Output: 2

# Access remaining seconds after full days
print("Seconds:", difference.seconds)  # Output: 16200 (4 hours 30 min in seconds)


#4:
from datetime import datetime
import pytz  # Module for timezone handling

# Define timezones
almaty_tz = pytz.timezone("Asia/Almaty")
ny_tz = pytz.timezone("America/New_York")

# Get current time in Almaty timezone
almaty_time = datetime.now(almaty_tz)
print("Time in Almaty:", almaty_time)  # Example: 2026-02-22 15:30:45+06:00

# Convert Almaty time to New York timezone
ny_time = almaty_time.astimezone(ny_tz)
print("Time in New York:", ny_time)  # Example: 2026-02-22 05:30:45-05:00
