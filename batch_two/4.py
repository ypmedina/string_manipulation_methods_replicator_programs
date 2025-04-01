#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same
#functionality without using upper() function.

user_inp = input("Please enter a word or sentence: ")

word = ""
for i in user_inp:
    if i.isupper():
        word += i
    else:
        word += i.swapcase()

print(word)

