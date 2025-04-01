#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do
#the same functionality without using rstrip() function.

user_inp = input("Enter a word/sentence: ")

right_strip = len(user_inp) - 1
while right_strip >= 0 and user_inp[right_strip] == ' ':
    right_strip -= 1

no_spaces = user_inp[:right_strip+1]

print(f"'{user_inp}'")
print(f"'{no_spaces}'")