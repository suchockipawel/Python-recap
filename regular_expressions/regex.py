import re

'''
# regex_exercise
# Task 1

Create a variable called text to store the data: Berlin is a world city of culture, politics, media and science. . 
Then search for the first white space character in the string and print its location using the appropriate label.

Your result should look like this:
The first white-space character is located at position: 6
'''

text = 'Berlin is a world city of culture, politics, media and science.'

## \s - Matches any whitespace character
pattern = re.search('\s', text)

## re.start() The method returns the index of the start of the matched substring
if pattern:
    first_whitespace = pattern.start()
    print("The first white-space character is located at position:", first_whitespace)
else:
    print("Not found")

print('\n')
'''
# Task 2:
Create a function that takes a string input as a number and replaces leading and trailing zeros.

Input/Output:
"0023.07623070"   -->   "23.0762307"  
"hello world"     -->   "hello world"  
"01230"           -->   "1230"  
'''

## re.sub(pattern,replacewith,string) The method replaces every pattern character (\s for space) with a replacewith character(s)

text1 = "0023.07623070"
print(re.sub("^0*(\\d+\\.\\d*?[1-9])0*$", r"\1", text1))

print('\n')
'''
# Task 3

this is a paragraph

In the bustling world of digital communication, emails serve as the lifeline of professional and personal correspondence. From boardrooms to living rooms, individuals rely on electronic messages to convey information swiftly and efficiently. JohnDoe123@example.com, a common placeholder, often finds itself at the forefront of test emails, representing the generic sender in countless trial messages. Meanwhile, JaneSmith456@gmail.com plays a similar role, popping up in various drafts and test scenarios across the virtual landscape. As emails traverse the cyber realm, TestUser789@hotmail.com emerges as another common character, standing in as a placeholder identity in the vast sea of trial messages. These digital avatars, like PlaceholderEmail1@domain.com and DummySender567@yahoo.com, dance through the interconnected web of communication as testers fine-tune the nuances of their messages. In the quest for email perfection, MessageTester987@mail.com and SenderPlaceholderXYZ@outlook.com take their turns, navigating the intricate pathways of the digital inbox. The symphony of electronic communication resonates with these fictional email personas, each contributing its part to the harmonious melody of the online exchange. Whether it's BusinessTestEmail789@domain.org or ExperimentMail456@protonmail.com, these dummy emails weave an intricate tapestry in the vast landscape of the digital communication ecosystem.


create a regex pattern to get all the email address from this paragraph.

'''

paragraph = "In the bustling world of digital communication, emails serve as the lifeline of professional and personal correspondence. From boardrooms to living rooms, individuals rely on electronic messages to convey information swiftly and efficiently. JohnDoe123@example.com, a common placeholder, often finds itself at the forefront of test emails, representing the generic sender in countless trial messages. Meanwhile, JaneSmith456@gmail.com plays a similar role, popping up in various drafts and test scenarios across the virtual landscape. As emails traverse the cyber realm, TestUser789@hotmail.com emerges as another common character, standing in as a placeholder identity in the vast sea of trial messages. These digital avatars, like PlaceholderEmail1@domain.com and DummySender567@yahoo.com, dance through the interconnected web of communication as testers fine-tune the nuances of their messages. In the quest for email perfection, MessageTester987@mail.com and SenderPlaceholderXYZ@outlook.com take their turns, navigating the intricate pathways of the digital inbox. The symphony of electronic communication resonates with these fictional email personas, each contributing its part to the harmonious melody of the online exchange. Whether it's BusinessTestEmail789@domain.org or ExperimentMail456@protonmail.com, these dummy emails weave an intricate tapestry in the vast landscape of the digital communication ecosystem."


emails = (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

#### step by step:

###1. \b: Word boundary anchor. Ensures that the pattern matches the entire email address and doesn't partially match within longer sequences of characters.

###2. [A-Za-z0-9._%+-]+: This part matches the local part of the email address before the @ symbol. 
#   Breakdown:
        # [A-Za-z0-9]: Any uppercase letter, lowercase letter, or digit.
        # ._%+-: These are allowed special characters in the local part of an email address.

###3. @: Matches the literal @ symbol, separating the local and domain parts of the email address.

### [A-Za-z0-9.-]+: This part matches the domain part of the email address after the @ symbol. 
    # Breakdown:
        # [A-Za-z0-9]: Any uppercase letter, lowercase letter, or digit.
        # .-: These are allowed special characters in the domain part of an email address.

###4. \.: Matches the literal dot (.) after the domain part, separating it from the top-level domain (TLD).

###5. [A-Z|a-z]{2,}: This part matches the top-level domain (TLD), which must consist of at least two letters (uppercase or lowercase). 
    # The | in [A-Z|a-z] is unnecessary and can be removed; it's treated as a literal character in this context.

###6. \b: Another word boundary anchor, ensuring that the pattern matches the entire email address.


pattern2 = re.findall(emails, paragraph)
print(pattern2)