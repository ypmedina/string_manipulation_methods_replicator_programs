#Prog10. rindex() return the first location of the function parameter in the string starting from the last
#character. Create a program that do the same functionality without using rindex() function.

user_inp = input("Enter a sentence: ")
find_index = input("Enter a word to find: ")

user_index = user_inp.rfind(find_index)

print(user_index)
