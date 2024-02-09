'''

### Task 1

Create a variable called `fruits` and one after another add the elements `Apples`, `Cherries` and `Strawberries`. 
Loop over the list `fruits` and print every element to the screen.

- Your result should look like this:

```
Apples
Cherries
Strawberries
```
'''

fruits = ['Apples', 'Cherries', 'Strawberries']
for fruit in fruits:
    print(fruit)
print("\n") 
'''
### Task 2

Create a variable `cities` which holds a list with the cities `London`, `Paris`, `Berlin` and `Amsterdam`. 
Print the sentence `The capital city of Germany is: Berlin` to the screen, using the string `Berlin` from the cities array.

- Your result should look like this:

```
The capital city of Germany is: Berlin
```

###
'''

cities = ['London', 'Paris', 'Berlin', 'Amsterdam']
print("The capital city of Germany is: ", cities[2])
print("\n") 

'''

### Task 3

Store the colors `cyan`, `magenta`, `green`, `yellow`, `black` and `white` in a list called `colors`. 
Remove the colors `green` and `white`. Print the remaining colors to the screen.

- Your result should look like this:

```
cyan
magenta
yellow
black
```

###

'''

colors = ['cyan', 'magenta', 'green', 'yellow', 'black', 'white']
colors.remove('green')
colors.remove('white')
for color in colors:
    print(color)
print("\n") 
'''
### Task 4

Store the letters `p`, `e`, `n`, `g`, `u`, `i`, `n` in a list. Combine those letters into a single string `penguin`. 
Capitalize that string and print it to the screen.

- Your result should look like this:

```
Penguin
```

###
'''


letters = ['p', 'e', 'n', 'g', 'u', 'i', 'n']
combined_string = ''.join(letters)
print(combined_string.capitalize())    
print("\n") 
'''
### Task 5

Store the names `pedro`, `eminem`, `nicholas`, `gerald`, `uranium`, `iniesta`, `nifemi` in a list. 
Sort the list so that they appear in ascending alphabetical order. 

- Your result should look like this:

```
eminem
gerald
iniesta
nicholas
nifemi
pedro
uranium

'''

names = ['pedro', 'eminem', 'nicholas', 'gerald', 'uranium', 'iniesta', 'nifemi']
names.sort()
for name in names:
    print(name)
