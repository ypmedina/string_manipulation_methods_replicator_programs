#Prog10. title() makes all first letter of each word in the string, capital letter.
#And all other letter in small case. Create a program that do the same functionality without using title() function.

#use split() and capitalize() to capitalize each starting letter

capitalized_words = []
user_inp = input("Please enter a word or sentence: ")
words = user_inp.split()

for i in words:
    capitalized_words.append(i.capitalize())

capitalized = " ".join(capitalized_words)

print(capitalized)