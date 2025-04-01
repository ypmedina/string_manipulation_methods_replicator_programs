#Prog06. ljust() add space characters at the end of the string to complete the number of characters
#specifies in function parameter. Create a program that do the same functionality without using ljust() function.

#huhuuu

user_inp = input("Please enter a word or sentence: ")

alignment = 50
output_str = user_inp + " " * (alignment - len(user_inp))

print(f"'{output_str}'")