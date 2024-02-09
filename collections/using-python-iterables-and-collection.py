'''
# Task - Maths with dictionary elements

You're given two dictionaries. Both have the same keys `a`, `b`, `c` with their values being random numbers. 
You need to multiply the values with the same key value in the other dict and sum all results.
'''

dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
}
result = 0
for key in dict1:
        result += dict1[key] * dict2[key]
print(result)



'''
# Task - Convert keys between cases

Different programming languages use different kind of schemes to name things. 
For example Python uses `snake_case`, JavaScript uses `camelCase`. 
You might also come across `kebap-case` - sometimes also called `dash-case`. 
You can read more about naming conventions in programming the [matching Wikipedia article](https://en.wikipedia.org/wiki/Naming_convention_(programming)).

When an API you are using is implemented using a different language 
it might not match Python's convention of naming things. 
Hence your task is to implement a method that converts a dictionary with natural cased keys like `A random key` to `a_random_key`.
'''
### Input A: 
natural_case = {
  'Company name': 'Digital Career Institute',
  'Street': 'Vulkanstraße',
  'House Number': 1,
  'City': 'Berlin'
}
def convert_to_snake_case(natural_case_dict):
    snake_case_dict = {}
    for key, value in natural_case_dict.items():
        snake_case_key = key.lower()
        snake_case_dict[snake_case_key] = value
    return snake_case_dict

snake_case_result = convert_to_snake_case(natural_case)
print(snake_case_result)

## Input B:

natural_case_2 = {
  'Movie name': 'James Bond 007: Skyfall',
  'Director': 'Sam Mendes',
  'Production Year': 2012,
  'Duration in minutes': 143,
  'Production countries': ['US', 'UK']
}
def convert_to_snake_case(natural_case_2_dict):
    snake_case_2_dict = {}
    for key, value in natural_case_2_dict.items():
        snake_case_2_key = key.lower()
        snake_case_2_dict[snake_case_2_key] = value
    return snake_case_2_dict

snake_case_2_result = convert_to_snake_case(natural_case_2)
print(snake_case_2_result)



'''
# Task - Matrix mean

You are given a two dimensional list of numbers. 
Calculate the mean of those numbers by implementing a 'mean' method that takes a list as an argument.
'''


numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]

def mean(numbers):
    mean_values = [sum(lists) / len(lists) for lists in numbers]
    return mean_values

result = mean(numbers)
print(result)


## Output:
# > mean(numbers)
#  [19, 65, 23, 90]


'''
# Task - Combine lists into a dict

You are given two lists. One with color names (`['red', 'green', 'blue']`) 
and the other one with their RGB hex value (`['#FF0000','#00FF00', '#0000FF']`). 
Create a combined dict `colors` from those two lists so that for example printing `colors['green']` shows `#008000` on the screen.
'''

color_names = ['red', 'green', 'blue']
color_hex = ['#FF0000','#00FF00', '#0000FF']

colors = dict(zip(color_names, color_hex))
print(colors)


'''
# Task - Highscore

You have a list of participants as strings. This list holds title-cased names. 
Alongside there is a dictionary with scores, using the same names as keys with a integer as their value.

Implement a method `get_score` that takes a name as an argument, verifies it is in the list of participants and then prints the name with the score.

If the participant can't be found print a message telling that.
'''


participants = ['Brian', 'Britney', 'Ben']
scores = {
  'brian': 25,
  'britney': 80,
  'ben': 50
}


def get_score(name):
    name = name.lower()
    if name in [participant.lower() for participant in participants]:
        print(f"{name.capitalize()} scored {scores[name]} points")
    else:
        print(f"{(name.capitalize())} did not participate.")

get_score('Paul')
get_score('Britney')



'''
# Task - Count characters

Implement a method called `count_characters`. It should accept any string and count how often each letter occurs in it.
'''

input_string = 'Elephant'

def count_characters(input_string):
    characters_count = {}
    for letter in input_string:
        characters_count[letter.lower()] = characters_count.get(letter.lower(), 0) + 1
    return characters_count

result = count_characters(input_string)
print(result)
