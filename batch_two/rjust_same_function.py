#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters
#specifies in function parameter. Create a program that do the same functionality without using rjust() function.

user_inp = input("Please enter a word or sentence: ")

alignment = 50
output_str = " " * (alignment - len(user_inp)) + user_inp

print(f"'{output_str}'")