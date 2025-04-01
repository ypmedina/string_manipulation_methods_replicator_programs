# Prog01. ltrip() remove the space characters at the beginning of the string. Create a program that do the
# same functionality without using lstrip() function.

# Create an if statement that reads spaces and moves to the right while making it stop when it reads a letter
# What the heck

sentence = "   No spaces here"
if sentence.startswith(" "):
    space_checker = 0
sentence = "    No spaces here"
if sentence:
    while space_checker < len(sentence) and sentence[space_checker] == ' ':
        # this line checks if the space_checker is still in bounds of the sentence and if it is reading a space or not
        space_checker += 1
output_sentence = sentence[space_checker:]

print(sentence)
print(output_sentence, "anymore")