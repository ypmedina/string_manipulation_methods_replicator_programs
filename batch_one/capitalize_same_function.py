#Prog09. capitalize() makes the first letter of the string, capital letter.
#And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

#maybe try using a for function and .upper() the first letter and .lower() all the other letters

user_inp = input("Please enter a word or sentence: ")

capitalized = ""
for i in range(len(user_inp)):
    if i == 0:
        capitalized += user_inp[i].upper()
    else:
        capitalized += user_inp[i].lower()

print(capitalized)