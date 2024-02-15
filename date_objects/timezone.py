# Let's go through some examples to demonstrate how to work with time zones in Python using the pytz module:

# 1. Getting Current Time in a Specific Time Zone:
#Suppose we want to get the current time in New York time zone:

import pytz
from datetime import datetime

# Get the New York time zone
tz_ny = pytz.timezone('America/New_York')

# Get the current time in New York time zone
current_time_ny = datetime.now(tz_ny)
print("Current time in New York:", current_time_ny)

# Converting Time Zone:
# Let's convert the current time in New York to UTC:

# Get the UTC time zone
tz_utc = pytz.timezone('UTC')

# Convert the current time in New York to UTC
current_time_utc = current_time_ny.astimezone(tz_utc)
print("Current time in UTC:", current_time_utc)

# Displaying Time in a Specific Format with Time Zone:
# Now, let's display the current time in New York and UTC in a specific format:

# Display the current time in New York and UTC with time zone information
formatted_time_ny = current_time_ny.strftime("%Y-%m-%d %H:%M:%S %Z %z")
print("Formatted time in New York:", formatted_time_ny)

formatted_time_utc = current_time_utc.strftime("%Y-%m-%d %H:%M:%S %Z %z")
print("Formatted time in UTC:", formatted_time_utc)

# Handling Time Zone Aware Datetimes:
#Finally, let's create a time zone aware datetime object for a specific date and time:

# Create a time zone aware datetime object for a specific date and time in New York time zone
localized_time = tz_ny.localize(datetime(2023, 1, 1, 12, 0, 0))
print("Localized time:", localized_time)