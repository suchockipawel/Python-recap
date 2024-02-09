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