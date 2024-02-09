'''
# Task 1:
create set
create set with keword set and add some objects to this set
'''
set_1 = set()

set_1.add(1)
set_1.add(2)
set_1.add(3)
set_1.add(4)
print(set_1)

print('\n')
'''
# Task 2:
access value from set
'''

# Creating a set
set_2 = {1, 2, 3, 'mango', 5}

to_check = 'mango'
if to_check in set_2:
    print(f"{to_check} is in the set_2.")
else:
    print(f"{to_check} is not in the set_2.")

print('\n')
'''
# Task 3:
add multiple values to set at once
'''
set_3 = {1, 2, 3}
set_3.update({4, 5, 6})

print(set_3)

print('\n')
'''
# Task 4:
write the difference between remove and discard with example
'''

set_4 = {'a', 'b', 'c', 'd', 'e'}

set_4.remove('b') # In .remove() method the element 'b' is removed from the set because is included in set_4, for all elements, which are not incl. in set_4, will be Error.
print(set_4)

set_4.discard('f') #  In .discard() method if the element is not present in set_4, it does not raise an error.
print(set_4)

print('\n')
'''
# Task 5:
create two sets and get the objects which are available in set a and set b
'''

set_5 = {1, 2, 3, 4, 'apple'}
set_6 = {'orange', 'apple', 'mango', 4, 5, 6, 7}

print(set_5.intersection(set_6))

print('\n')

'''
# Task 6:
find the difference between 
1. difference vs difference_update
2. intersection vs intersection_update
3. symmetric_difference   symmetric_difference_update

please add the examples as well.
'''
set_7 = {'name','age', 'city', 'country'}
set_8 = {'city', 'street', 'number'}


print(set_7.difference(set_8))
print(set_7.intersection(set_8))
print(set_7.symmetric_difference(set_8))


set_9 = {'name','age', 'city', 'country'}
set_10 = {'city', 'street', 'number'}

print(set_9.difference_update(set_10))
print(set_9.intersection_update(set_10))
print(set_9.symmetric_difference_update(set_10))


