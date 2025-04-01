# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter.
# Create a program that do the same functionality without using removeprefix() function.

# To make it easier, just ask the user what is the prefix in the word and remove it

user_input = input("Please enter a word")
user_prefix = input("What is the prefix used in the word? If none, please press enter")
user_input = input("Please enter a word: ")
user_prefix = input("What is the prefix used in the word? If none, please press enter: ")

if user_prefix and user_input.startswith(user_prefix):

    no_prefix = user_input[len(user_prefix):]
else:
    no_prefix = user_input

print(no_prefix)