import re

# Task 1

# Search for the first white-space character in the string

text = "Berlin"
x = re.search("\s", text)
if x:
    print("The first white-space character is located in position:", x.start())

# Task 2

'''
NOTE: We can use \b to remove 0 from string but the issue with using \b is it will replace all zeros from string so we have to create a patteren to get the desire results.

'''

given_string = "0023.07623070"
print(re.sub("^0*(\\d+\\.\\d*?[1-9])0*$", r"\1", given_string))

# Nina's Solution. I really like it as its very simple one.
def replace_zeros(string_input):
    pattern = re.sub(r'^0+|0+$', '', string_input)
    return pattern

string_input = "0023.07623070"
result = replace_zeros(string_input)
print(result)

# Task 3

long_string = "In the bustling world of digital communication, emails serve as the lifeline of professional and personal correspondence. From boardrooms to living rooms, individuals rely on electronic messages to convey information swiftly and efficiently. JohnDoe123@example.com, a common placeholder, often finds itself at the forefront of test emails, representing the generic sender in countless trial messages. Meanwhile, JaneSmith456@gmail.com plays a similar role, popping up in various drafts and test scenarios across the virtual landscape. As emails traverse the cyber realm, TestUser789@hotmail.com emerges as another common character, standing in as a placeholder identity in the vast sea of trial messages. These digital avatars, like PlaceholderEmail1@domain.com and DummySender567@yahoo.com, dance through the interconnected web of communication as testers fine-tune the nuances of their messages. In the quest for email perfection, MessageTester987@mail.com and SenderPlaceholderXYZ@outlook.com take their turns, navigating the intricate pathways of the digital inbox. The symphony of electronic communication resonates with these fictional email personas, each contributing its part to the harmonious melody of the online exchange. Whether it's BusinessTestEmail789@domain.org or ExperimentMail456@protonmail.com, these dummy emails weave an intricate tapestry in the vast landscape of the digital communication ecosystem."
patteren = re.compile("\w+[?=@]+\w*.\w*")
result = patteren.findall(long_string)
print(result)


def replace_zeros(string_input):
    pattern = re.sub(r'^0+|0+$', '', string_input)
    return pattern

string_input = "0023.07623070"
result = replace_zeros(string_input)
print(result)
