#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same
#functionality without using lower() function.

#use the casefold() function

user_input = input("Enter a sentence in all caps: ")

lowercase = user_input.casefold()

print(lowercase)