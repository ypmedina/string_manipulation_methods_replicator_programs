#Prog05. endswith() check if the string end part matches the function parameter.
#Create a program that do the same functionality without using endswith() function.

#get 2 user inputs and make the user enter the suffix so that the program can check if it is there
user_inp = input("Enter a word or sentence: ")
word_end = input("Enter the last part of your word or sentence to check: ")

if user_inp[-len(word_end):] == word_end:
    print("The string ends with the given letter/word.")
else:
    print("The string does not end with the given letter/word.")