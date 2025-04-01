#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same
#functionality without using isupper() function.

#use swapcase() and use islower() to check it its all uppercase

user_inp = input("Please enter a word or sentence: ")

if user_inp.swapcase().islower():
    print("You entered all capital letters")
else:
    print("You did not enter all capital letters")