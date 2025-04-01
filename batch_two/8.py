#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters
#specifies in function parameter. Create a program that do the same functionality without using zfill() function.

user_inp = input("Please enter a word or sentence: ")
user_fill = int(input("Please enter how many zeroes you want to fill the word/sentence with: "))
zero = chr(48)

print(((user_fill - len(user_inp)) * zero)  + user_inp)
