# scope 

#The provided Python code covers the concept of scope in Python, including global scope variables, mutable and immutable objects, function scopes, and first-class functions. Let's summarize each part with explanations:

# Global Scope:
#Global variables like my_name and course are defined outside of any function and can be accessed from any part of the code.

my_name = "Majid"

def my_function():
    print(my_name) # accessing global variable within a function 

my_function() 
print(my_name)    

#Function Scope:
#Variables defined within a function are local to that function and cannot be accessed from outside. Example: my_function.
def my_function():
    local_variable = 'Local Variable'
    print(local_variable)
my_function()    

#Mutable vs. Immutable Objects:
#Immutable objects like strings (course) and mutable objects like lists (new_var) behave differently when passed as function arguments or used as default parameters.

course = 'Python' # Immutable string

def change_course(course):
    course = 'Java' # Assigning a new value to the parameter 'course'
    print(course)

change_course(course) # Output:Java 
print(course) # Output: Python (global variable remains unchanged)  

new_var = [0, 1] # mutable list

def update_new_var(new_var):
    new_var.append(2)  # Modifying the list passed as argument
    print(new_var)

update_new_var(new_var) 
print(new_var)   

#Default Parameters with Mutable Objects:
#When using mutable objects as default parameters in a function definition (e.g., some_list_name=[]), the same list object is shared across multiple function calls.

def mutable_obj(some_list_name=[]):
    some_list_name.append(23)
    print(some_list_name)

mutable_obj()  # Output: [23]
mutable_obj()  # Output: [23, 23] (unexpected behavior due to default mutable parameter)


#Calling Functions within Functions:
#Functions can call other functions defined within their scope. Example: print_course calling print_city.

def outer():
    def inner():
        print('Inner function')
    
    inner()  # Calling inner function within outer function

outer()  # Output: Inner function


#First-Class Functions:
#Functions are first-class citizens in Python, meaning they can be passed as arguments to other functions, returned from functions, and assigned to variables. Example: my_new_city.

def print_city(city_name='Berlin'):
    print(city_name)

my_new_city = print_city  # Assigning function to a variable
my_new_city()  # Output: Berlin


#Functions as Arguments:
#Functions can be passed as arguments to other functions. Example: operations.

def operations(*args, fun):
    fun(args)

def add(list_of_numbers):
    print(sum(list_of_numbers))

operations(1, 2, 3, 4, 5, fun=add)  # Output: 15 (sum of numbers passed as arguments)