#Prog09. index() return the first location of the function parameter in the string.
#Create a program that do the same functionality without using index() function.

user_inp = input("Enter a sentence: ")
find_index = input("Enter the substring to find: ")

user_index = user_inp.find(find_index)

print(user_index)
