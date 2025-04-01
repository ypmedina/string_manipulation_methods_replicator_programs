#Prog10. rindex() return the first location of the function parameter in the string starting from the last
#character. Create a program that do the same functionality without using rindex() function.

user_inp = input("Enter a sentence: ")
find_index = input("Enter a word to find: ")

user_index = -1
for i in range(len(user_inp) - 1, -1, -1):
    if user_inp[i:i+len(find_index)] == find_index:
        user_index = i
        break

if user_index != -1:
    print(f"'{find_index}' is indexed at {user_index}.")
else:
    print(f"'{find_index}' not found in the string.")
