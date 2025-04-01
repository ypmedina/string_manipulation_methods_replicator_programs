#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
#use swapcase and isupper to check

user_inp = input("Please enter a word or sentence: ")
user_swapped = user_inp.swapcase()

if user_swapped.isupper():
    print("Your word/sentence has all lowercase letters")
else:
    print("Your word/sentence is not all lowercase")