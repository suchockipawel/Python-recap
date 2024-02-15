#Iteration (looping) through lists and dictionaries.
#Unpacking data from iterables (lists, tuples).
#Enumerating through iterables using enumerate.
#Zipping multiple iterables together.
#Built-in functions such as sum, max, any, and all.
#Functional programming concepts like map and filter.

list_of_colors = ["red", "green", "blue"]
list_of_iterables = ("list", "tuple", "set", "dictionary", "string")
days_of_the_week = (("mon", "Monday"), ("Tue", "Tuesday"), ("Wed", "Wednesday"),)
set_of_items = {"john", "fred", "peter"}
first_name = "john"
data_of_persons = [["John", "doe", 18, "germany"], ["Mike", "doe", 28, "China"]]

# Approach 1: Unpacking everything from the loop statement
for f_name, l_name, age, country in data_of_persons:
    print(f_name, age, country)

# Approach 2: Indexing and no unpacking
for item in data_of_persons:
    print(item[0], item[2], item[3])

# Approach 3: Looping with unpacking inside the loop
for person in data_of_persons:
    first_name, _, age, country = person
    print(first_name, age, country)

# Approach 4: Slicing
for person in data_of_persons:
    first_name = person[0]
    age, country = person[2:]
    print(first_name, age, country)

# Approach 5: Nested loop
for person in data_of_persons:
    for index in range(len(person)):
        if index == 1:
            continue
        print(person[index])

phonebook = {"james": "846775785", "grace": "859463653", "alba": "64655353"}

# Looping through keys and values using .items()
for name, number in phonebook.items():
    print(name, number)

# Enumerating through a dictionary
for index, (name, number) in enumerate(phonebook.items()):
    print(index, name, number)

# Zipping multiple iterables together
names = ["paul", "rosemary", "james"]
countries = ("germany", "America", "japan")
age = {18, 65, 22}
colors = ["black", "white" , "grey"]
for result in zip(names, countries, age, colors):
    print(result)

# Functions like max, sum, min
scores = [34, 22, 89, 67, 75]
numbers = (56, 23, 10, 100, 89.3)
students = ["mike", "roselyn", "abigail", "zainab", "elizabeth"]
random_data = (89, "germany", "red", 45)
print(sum(scores))
print(max(numbers))

# Any and all functions
empty_list = []
bad_list = (0, "")
average_list = [0, 89, "ruth"]
good_list = {200, 546, "chris"}
print(any(empty_list), all(empty_list))

# Map function
scores = [34, 22, 89, 67, 75]
students = ["mike", "roselyn", "abigail", "zainab", "elizabeth"]
def add_value(input):
    return input.upper()
for item in map(add_value, students):
    print(item)

# Filter function