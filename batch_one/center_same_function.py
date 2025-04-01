#Prog07. center() add space characters at the beginning and at the end of the string to print the
#string at the center. Create a program that do the same functionality without using center() function.

#idk man

user_inp = input("Please enter a word or a sentence: ")
width = 50
spaces = (width - len(user_inp)) //2
centered = f'{' ' * spaces}{user_inp}{' ' * spaces}'

print(centered)