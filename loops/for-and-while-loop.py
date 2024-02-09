'''

# Task 1 - reverse word
Your task is to write a Python program that accepts a word from the user and reverses it, using a for loop.

Hint: the range() function accepts negative numbers!

Your results should look like this:
Input a word to reverse: hello
Reversed word: olleh
'''

input_word = input("Input a word to reverse: ")
reversed_word = ""

# starting point =-1 #starting index.
# ending point =-1 #stopping index.
# step =-1 #step size.

# the three occurrences of -1 in the range function work together to iterate through the characters of the original word in reverse order. 
# The loop starts at the last character, stops at the first character, and moves backward one character at a time.

for letter in range(len(input_word) -1, -1, -1):
    reversed_word += input_word[letter]
print("Reversed word:", reversed_word)




'''
# Task 2 - count digits and letters
Your task is to write a Python program using for loop, that counts digits and letters.
User should be prompted to enter her/his characters with the keyboard, even without looking at it.
Store the information about number of digits and letters in some variables.

Hint: use one of the string's method and try to type only letters and digits!

Your results could look like this:
Input your characters: dgbudf8gsdf7g8sd7fg7dsf7g7y7df7ygsdfg775uybgfbfdug8fdsugdfsguf7g7df7g7ydf7yg7rye7gy7eryg
Number of digits:  21
Number of letters:  67 
'''


user_input = input("Input your characters: ")

digit_count = 0
letter_count = 0

for x in user_input:
    if x.isdigit():
        digit_count += 1
    elif x.isalpha():
        letter_count += 1

print("Number of digits:", digit_count)
print("Number of letters:", letter_count)


'''
# Task 3 - Upper and lower letters
Your task is to write a Python program using while loop, that iterates over given string and converts the lower letters to capital letters and vice versa.
Print it out after changes.

Hint: use string's methods and be careful of long texts and new lines!

Note: You can use any text, for example from lyrics. My was:
"Overhead the albatross Hangs motionless upon the air And deep beneath the rolling waves In labyrinths of coral caves" 😃

Your results should look like this:

oVERHEAD THE ALBATROSS hANGS MOTIONLESS UPON THE AIR aND DEEP BENEATH THE ROLLING WAVES iN LABYRINTHS OF CORAL CAVES
'''

string = "Overhead the albatross Hangs motionless upon the air And deep beneath the rolling waves In labyrinths of coral caves"


index = 0

while index < len(string):
    if string[index].isupper():
        string = string[:index] + string[index].lower() + string[index+1:]
    elif string[index].islower():
        string = string[:index] + string[index].upper() + string[index+1:]
    index += 1

print(string)




'''
# Task 4 - find divisible numbers
'''


divisible_count = 0

while True:
    a = int(input("Type starting integer: "))
    b = int(input("Type ending integer: "))
    c = int(input("Type divisor: "))
    
    if c == 0:
        break
    print()
    current_number = a
    while current_number <= b:
        if current_number % c == 0:
            print(current_number, " is divisible by", c)
            divisible_count += 1
        current_number += 1
    print()

print("Total count of divisible numbers:", divisible_count)