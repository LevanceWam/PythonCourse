from pprint import pprint
# Exercise 1 write a program that will find the most repeated character in the text
sentence = "This is a common interview question"

# my attempt
letters = [*sentence]
print(letters.count("i"))

# video Solution
# make it into a dictionary
char_frequncy = {}

for char in sentence:
    if char in char_frequncy:
        # if we see a repeat add 1 to it
        char_frequncy[char] += 1
    else:
        # if we don't see the character add a 1 to it
        char_frequncy[char] = 1
# this is for the console to improve readability
pprint(char_frequncy, width=1)

# Since dictionaries doesn't put the objects in indexes we will turn it into a tuple
# Then we will sort it out and reverse it to get the highest character first
char_frequncy_sorted = sorted(
    char_frequncy.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_frequncy_sorted)
