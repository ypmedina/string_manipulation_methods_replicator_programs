#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter.
#Create a program that do the same functionality without using removesuffix() function.

user_inp = input("Please enter a word: ")
user_suffix = input("What is the suffix of this word?: ")

if user_inp.endswith(user_suffix):
    no_suffix = user_inp[: -len(user_suffix)]
    print(f"{no_suffix} is the final word")
else:
    print(f"{user_inp} is the final word")
