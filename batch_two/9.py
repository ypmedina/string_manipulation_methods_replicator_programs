#Prog08. count() return how many time the function
#parameter appear in the string. Create a program that do the same functionality without using count() function.

count_list = 0

user_input = input("Enter a word/sentence:")
user_count = input("What letter/word would you like to be counted?: ")

for i in user_input:
    if i == user_count:
        count_list += 1


print(f"{count_list} {user_count}'s were in the word/sentence")