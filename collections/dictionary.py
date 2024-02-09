'''
# Task 1

Create a dictionary which contain multi type keys as well as values
'''
dict_1 = {'age': 45, 'is_true': True, 175.5: 'hight'}
print(dict_1)

print('\n')
'''
# Task 2

list_of_keys = ['first_name', 'last_name', 'address', 'City', 'country']

create a dictionary with the keys from list_of_keys, the value should be none.
hint: use method fromkeys
'''
list_of_keys = ['first_name', 'last_name', 'address', 'City', 'country']

dict_2 = dict.fromkeys(list_of_keys, None)

print(dict_2)

print('\n')
'''
# Task 3
create empty dictionary
use setdefault method to add items to dictionary  
print the values for the key you added
update the the value of key you added in step 2
print the whole dictionary
'''

dict_3 = {}
dict_3.setdefault('name', 'pawel')
print(dict_3)

dict_3['name'] = 'Pawel'
print(dict_3)

print('\n')
'''
# Task 4

Write the difference between getting the values from dictonary using key as an index method and get() method. with examples
'''

dict_4 = {'first_name': 'Pawel', 'last_name': 'Suchocki', 'age': 45}

first_name = dict_4['first_name']
age = dict_4['age']
print(first_name)
print(age)

first_name = dict_4.get('first_name')
age = dict_4.get('age')
print(first_name)
print(age)


print('\n')
'''
# Task 5

get the list of values from dictionary 
get the items from a dictionary 
'''

dict_5 = {'age': 45, 'is_true': True, 175.5: 'height'}

values_list = list(dict_5.values())
items_list = list(dict_5.items())

print(values_list)
print(items_list)

print('\n')
'''
# Task 6

print the 3rd dictionary items from inner_dict_3
'''

nested_dict = {
    'outer_dict_1': {
        'inner_dict_1': [ 
            {'key1': 'value1'},
            {'key2': 'value2'},
            {'key3': 'value3'}
        ],
        'inner_dict_2': [  
            {'key4': 'value4'},
            {'key5': 'value5'}
        ]
    },
    'outer_dict_2': {
        'inner_dict_3': [ 
            {'key6': 'value6'},
            {'key7': 'value7'},
            {'key8': 'value8'}
        ]
    }
}

print(nested_dict['outer_dict_2']['inner_dict_3'][2])

data = [('1', '2', '3', '4'), ('5', '6', '7', '8')]

for items in data:
    var1, var2, var3, var4 = items
    print(var1, var3, var4)

names = ['paul']