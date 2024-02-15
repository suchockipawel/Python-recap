# Adding Days to Current Date:

# Adding Days to Current Date
import datetime

add_number_of_days = 3
current_date = datetime.date.today()  # Get current date
new_date_with_day = current_date + datetime.timedelta(days=add_number_of_days)  # Add days to current date
print("New Date with Added Days:", new_date_with_day)  # Print the new date

# Calculating Difference Between Dates
date_1 = datetime.date(2023, 9, 27)  # Define a date
date_2 = datetime.date.today()  # Get current date
number_of_days_into_the_course = date_2 - date_1  # Calculate difference between dates
print("Number of Days into the Course:", number_of_days_into_the_course)  # Print the difference

# Calculating Total Days Between Dates
start_date = datetime.date(2023, 9, 27)  # Define start date
end_date = datetime.date(2024, 10, 17)  # Define end date
total_days = end_date - start_date  # Calculate total days between dates
print("Total Days Between Dates:", total_days)  # Print the total days

# Calculating Time Difference Between Datetimes
datetime1 = datetime.datetime(2023, 11, 1, 12, 0, 0)  # Define datetime
datetime2 = datetime.datetime(2023, 11, 10, 16, 30, 0)  # Define another datetime
time_difference = datetime2 - datetime1  # Calculate time difference
print("Time Difference:", time_difference)  # Print the time difference

# Calendar Operations
import calendar

# Getting Month Calendar
month_calendar = calendar.month(theyear=2023, themonth=2)  # Get month calendar
print("Month Calendar:", month_calendar)  # Print the month calendar

# Getting Weekday
week_day = calendar.weekday(year=2023, month=9, day=23)  # Get weekday
print("Weekday:", week_day)  # Print the weekday

# Determining Number of Days in a Month
days_in_month = calendar.monthrange(year=2023, month=6)  # Get days in month
print("Days in Month:", days_in_month)  # Print the days in month

# Checking Leap Year
year = 2025
is_leap_year = calendar.isleap(year)  # Check if year is leap year
print(f"{year} is a leap year" if is_leap_year else f"{year} is not a leap year")  # Print leap year status