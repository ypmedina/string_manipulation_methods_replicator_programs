#Prog08. swapcase() reverse the casing of each of the character of the string.
#Create a program that do the same functionality without using swapcase() function.

#Use a for function to get each letter's case and use .lower() and .upper() to case swap

user_inp = input("Enter a word or sentence: ")

swapped_case = ""
for i in user_inp:
    if i.islower():
        swapped_case += i.upper()
    else:
        swapped_case += i.lower()

print(swapped_case)