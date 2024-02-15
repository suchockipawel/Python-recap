# Strings 
# Define the strings
first_name = 'majid'
last_name = 'bahader'
city = "Göttingen"
country = 'Germany'

# Print each string
print("First Name:", first_name)
print("Last Name:", last_name)
print("City:", city)
print("Country:", country)

# Concatenation
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Repetition
repeated_country = country * 4
print("Repeated Country:", repeated_country)

# Indexing
print("First Character of First Name:", first_name[0])  # Positive indexing
print("Last Character of First Name:", first_name[-1])  # Negative indexing

# Slicing
print("First 6 Characters of Country:", country[:6])  # Simple slicing
print("Third to Fifth Characters of Country:", country[2:5])  # Simple slicing

# Looping through characters
print("Characters in Country:")
for char in country:
    print(char)

# Special attributes/methods
print("Methods and Attributes of String:", dir(country))

# Immutable nature of strings
capitalized_country = country.capitalize()
print("Capitalized Country:", capitalized_country)
print("Original Country (Still Unchanged):", country)