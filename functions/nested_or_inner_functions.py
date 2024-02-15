# Nested or inner functions in Python are functions defined within the scope of another function, known as the outer or parent function. 

# These inner functions are only accessible from within the outer function and are usually used to encapsulate logic that is closely related to the outer function.

def get_age(age):
    # inner functions to add a value to the age
    # get_age Function: It takes an age as input and defines an inner function add_to_age to add 10 to the age.

    def add_to_age(value):
        result = value + 10
        return result 
    
    # Calling the inner function to add 10 
    # It then calls this inner function and returns the new age.

    new_age = add_to_age(age)
    return new_age

# get_full_name Function: It takes first name and last name as inputs, concatenates them, and defines an inner function remove_spaces to strip any spaces from a string. This inner function modifies the full_name variable using the nonlocal keyword.

def get_full_name(first_name, last_name): # Outer or parent function 
    full_name = first_name + last_name + " "
    print(f"From inside get_full_name 1: {full_name}")

     # Inner function to remove spaces from a string
    def remove_spaces(item: str):
        value = item.strip()
        # Modifying the outer variable full_name using nonlocal keyword
        nonlocal full_name
        full_name = "Just another string"
        print(f"From inside remove_spaces 2: {full_name}")
        return value
    
    # # Calling the inner function to remove spaces from the full_name
    new_name = remove_spaces(full_name)
    # Notice that full_name has been modified by the inner function
    print(f"From inside get_full_name 2: {full_name}")
    
    return full_name

# # Calling the get_age function

# Output: The get_full_name function is called with f_name and l_name, and the modified full_name is printed. Similarly, the get_age function is called with age, and the new age after adding 10 is printed.
age = 25
new_age = get_age(age)
print(new_age)

# In summary, nested functions in Python provide a way to encapsulate logic and maintain the state within the scope of the outer function. They are particularly useful for organizing code and avoiding global namespace pollution.