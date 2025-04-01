#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that
#do the same functionality without using startswith() function.

user_inp = input("Enter a word or sentence: ")
word_start = input("Enter the last part of your word or sentence to check(case sensitive): ")

if user_inp[:len(word_start)] == word_start:
    print("The string starts with the given letter/word.")
else:
    print("The string does not start with the given letter/word.")