# In Python, dates are typically handled using the datetime module, which provides classes for manipulating dates and times. 

# 1 Importing the datetime Module:
#First, you need to import the datetime module:

import datetime

# 2. Creating Date Objects:
#You can create date objects using the datetime.date class. Specify the year, month, and day as arguments:

# Create a date object for January 1, 2023
my_date = datetime.date(2023, 1, 1)

# 3. Getting Current Date:
#You can get the current date using the datetime.date.today() method:

# Get the current date
current_date = datetime.date.today()

# 4. Accessing Date Components:
# You can access individual components of a date object (year, month, day) using attributes:

year = my_date.year
month = my_date.month
day = my_date.day

# 5. Formatting Dates:
#You can format date objects as strings using the strftime() method, which accepts a format string:

formatted_date = my_date.strftime("%Y-%m-%d")
#Here, '%Y represents the year with century, %m represents the month (zero-padded), and %d represents the day of the month (zero-padded).

# 6. Parsing Dates from Strings:
#You can parse date strings into date objects using the strptime() method, which also accepts a format string:

date_string = "2023-01-01"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()

from datetime import datetime, date

# Current local date and time
current_datetime = datetime.today()
print("Current Date and Time:", current_datetime)

# Current local date
current_date = date.today()
print("Current Date:", current_date)

from datetime import datetime

# Convert string to datetime
string_date_time = "2023-11-01 14:30:00"
iso_format_datetime = datetime.fromisoformat(string_date_time)
print("Converted Datetime:", iso_format_datetime)

from datetime import datetime

# Convert datetime to string
iso_to_string_format = datetime.isoformat(iso_format_datetime)
print("Converted String:", iso_to_string_format)

from datetime import datetime, date

# Creating Custom Date and Time Objects:
# Custom date object
start_date_of_python_course = date(2023, 9, 27)
print("Custom Date:", start_date_of_python_course)

# Custom date and time object
start_date_time_of_python_course = datetime(2023, 9, 27, 9, 0, 0, 2333)
print("Custom Date and Time:", start_date_time_of_python_course)

from datetime import datetime
#Parsing String to Datetime Object:

# Parse string to datetime object
datetime_by_name = 'Mon 18 Jan 2023'
datetime_by_name_str_dt = datetime.strptime(datetime_by_name, '%a %d %b %Y')
print("Parsed Datetime:", datetime_by_name_str_dt)