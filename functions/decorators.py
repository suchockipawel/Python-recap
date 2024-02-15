# Decorator
# Definition: Decorators are functions that add functionality to another function without modifying its code directly.

# decorator from a closure 

# Definition of my_decorator: Here, we define a decorator function named my_decorator, which takes another function any_function as its argument. This function will be used to decorate other functions.
def my_decorator(any_function):
    print("inside my_decorator")

    # Inner function within the decorator

    # Inner Function do_something: Within my_decorator, we define an inner function called do_something. This inner function modifies the behavior of the original function (get_full_name) by adding additional functionality.

    def do_something(*args, **kwargs):
        print("Inside do_something")
        new_first_name = args[0] + " ####"
        new_last_name = args[1] + " ----"
        new_args = [new_first_name, new_last_name]
        return any_function(*new_args, **kwargs)
    
    return do_something

# Function to be decorated

# Usage of @my_decorator: The @my_decorator syntax is a shorthand way to apply the my_decorator to the get_full_name function. It's equivalent to get_full_name = my_decorator(get_full_name).
@my_decorator
def get_full_name(first_name, last_name):
    print("Finally called get full name")
    full_name = first_name + " " + last_name
    print(f"My full name is {full_name}")
    return full_name

# Call the decorated function

# Execution Flow: When get_full_name is called with first_name and last_name, it actually invokes do_something, which modifies the arguments and calls the original get_full_name function with the modified arguments.
last_name = "Doe"
first_name = "John"
result = get_full_name(first_name, last_name)
print(result)

# Inner Function Behavior: The inner function do_something adds decorations ("####" and "----") to the first_name and last_name, respectively.

# Output: The original get_full_name function prints the full name with additional decorations. Finally, it returns the decorated full name.

# In summary, the decorator my_decorator adds extra functionality to the get_full_name function without modifying its core logic. It's a powerful tool in Python for dynamically extending the behavior of functions.
