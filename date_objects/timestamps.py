 # Using the time Module:

# The time module provides functions for working with timestamps, such as getting the current timestamp and converting timestamps to human-readable formats.

import time

# Get the current timestamp (seconds since the epoch)
current_timestamp = time.time()
print("Current timestamp:", current_timestamp)

# Convert a timestamp to a human-readable format
formatted_time = time.ctime(current_timestamp)
print("Formatted time:", formatted_time)

# Using the datetime Module:
# The datetime module provides classes for representing dates, times, and timestamps. You can create a datetime object representing a specific point in time and convert it to a timestamp.

from datetime import datetime

# Create a datetime object representing a specific point in time
specific_datetime = datetime(2022, 1, 27, 10, 30, 0)

# Convert the datetime object to a timestamp
timestamp = specific_datetime.timestamp()
print("Timestamp:", timestamp)

# 3. Converting Timestamp to datetime Object:
# You can convert a timestamp to a datetime object using the fromtimestamp() method.

# Convert a timestamp to a datetime object
converted_datetime = datetime.fromtimestamp(timestamp)
print("Converted datetime:", converted_datetime)

# 4. Working with Milliseconds:
# Timestamps can also be represented with milliseconds. You can use the time() method from the datetime module to get the current time with milliseconds.

# Get the current time with milliseconds
current_time_with_ms = datetime.now().time()
print("Current time with milliseconds:", current_time_with_ms)

# These examples illustrate how to work with timestamps in Python using the time and datetime modules. Timestamps provide a convenient way to represent and manipulate time-related information in Python applications.