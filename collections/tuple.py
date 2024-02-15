# Tuples in Python

# Empty Tuple: Defines an empty tuple using both empty parentheses and the tuple() keyword.
#Convert Iterable to Tuple: Converts the string 'Hello' into a tuple using the tuple() function.
#Change Object in List (Mutable): Demonstrates how to modify a list within a tuple. In this case, the last element of a list derived from the string 'Hello' is changed from 'o' to 'a'.
#Multi-type Tuple: Defines a tuple with elements of different data types.
#Nested Tuple: Illustrates a tuple containing another tuple as one of its elements.
#Access Objects from Tuple: Shows how to access elements of a tuple using indexing.
#Modify List within Tuple: Modifies a list that is an element of a tuple.
#Index and Count Methods: Utilizes the index() and count() methods to find the index of an object and count the occurrences of a specific value, respectively.
#Comparing Tuples: Compares two tuples for equality.
#Each section is commented to explain its purpose and functionality, enhancing the understanding of tuple manipulation in Python.

# Define an empty tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# Define a tuple using the tuple keyword
empty_tuple_using_keyword = tuple()
print("Empty Tuple Using Keyword:", empty_tuple_using_keyword)

# Convert an iterable to a tuple
word = 'Hello'
word_tuple = tuple(word)
print("Tuple from Word:", word_tuple)

# Change an object in a list (mutable)
word_list = list(word)
word_list[-1] = 'a'
print("Word List after Change:", word_list)

# Multi-type tuple
multi_type_tuple = (2, 'string', 12.00, False)
print("Multi-type Tuple:", multi_type_tuple)

# Nested tuple
nested_tuple = ('Hello', 'world', (1, 2, 3))
print("Nested Tuple:", nested_tuple)

# Access objects from a tuple
print("Accessing Element at Index 1:", nested_tuple[1])

# Access nested object from a tuple
print("Accessing Nested Element:", nested_tuple[2][1])

# Multi-nested tuple
multi_nested_tuple = ('Hello', 'world', (1, ('python', 'java', 'html', 'css'), 3))
print("Multi-nested Tuple:", multi_nested_tuple[2][1][2])

# Modify list within a tuple
list_within_tuple = (1, 2, 3, ['python', 'java', 'html', 'css'], 4, 5, 6)
list_within_tuple[3][1] = 'javascript'
print("Modified List within Tuple:", list_within_tuple)

# Use index method to access the index of an object
new_tuple = (1, 5, 6, 8, 6, 6)
index_of_object = new_tuple.index(6)
print("Index of Object:", index_of_object)

# Use count method to count the number of occurrences
print("Count of 6:", new_tuple.count(6))

# Comparing tuples
tuple_1 = (1, 2, 3)
tuple_2 = (1, 2, 3)
print("Tuple 1 Type:", type(tuple_1))
print("Tuple 2 Type:", type(tuple_2))
print("Tuple Equality:", tuple_1 == tuple_2)

'''
Task 1: Create a Tuple and Access Elements
Create a tuple containing different types of elements and access each element by index.

'''

tuple_1 = ('Pawel', 1, 3.5, False, [10, 11, 12])

print(tuple_1[0])
print(tuple_1[1])
print(tuple_1[2])
print(tuple_1[3])
print(tuple_1[4])

'''
Task 2: Tuple Concatenation and Repetition
Create two tuples, concatenate them, and repeat the elements of one tuple.
'''
tuple_2 = (5, 3, 8)
tuple_3 = ('apple', 'banana', 'mango')

concatenated_tuple = tuple_2 + tuple_3
print(concatenated_tuple)

repeated_tuple = concatenated_tuple * 2
print(repeated_tuple)

'''
Task 3: Check Membership and Length
Create a tuple and check if an element exists within it. Also, find the length of the tuple.
'''
tuple_4 = (1, 'banana', 'mango', 6, 8)
to_check = 'apple'
if to_check in tuple_4:
    print(f'{to_check} exist in tuple')
else:
    print(f'{to_check} not exist in tuple')    

print(len(tuple_4))

'''
Task 4: Unpack and Create New Tuple
Unpack elements from a tuple, create a new tuple with the unpacked values, and perform an operation.
'''
tuple_5 = ('name', 'age', 3, 4)
print(tuple_5)

first_element = tuple_5[0]
second_element = tuple_5[1]
third_element = tuple_5[2]
fourth_element = tuple_5[3]


new_tuple = (first_element + second_element, fourth_element - third_element)
print(new_tuple)


'''
Task 5: Convert Tuple to List and Vice Versa
Create a tuple, convert it to a list, modify it, and then convert it back to a tuple.
'''

tuple_6 = ('Hello', 'world', 'python','java','html','css')
print(tuple_6)

converted_tuple_6 = list(tuple_6)
converted_tuple_6[1] = 'WebDevelopment'
converted_tuple_6.remove('Hello')


modified_tuple_6 = tuple(converted_tuple_6)
print(modified_tuple_6)