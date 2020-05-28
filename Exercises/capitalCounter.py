# Let's write a program that will count the amount of capital letters in a file
# By Levance Wamley jr
import random
import string

# First select the file we want to read
file = open('sample.txt')
data = file.read()
# returning the words in a list
words = data.split()
capitals = 0
lowers = 0

# Here we are going to iterate through the list and seperate the words
for word in words:
    # Now we are iterating through the word to get the letter in each word
    for letter in word:
        # if the letter is capital then we will count it if not then we'll give a point to the lowercase counter
        if letter.isupper():
            capitals += 1
        else:
            lowers += 1

print(f"There are {capitals} captial letters in the file.")
print(f"There are {lowers} lowercase letters in the file.")

# practice to get the understand how to get the amount of letters in a string
cap_letters = 0
low_letters = 0
sentence = "".join(random.choices(string.ascii_letters, k=20))
print(sentence)

for caps in sentence:
    if caps.isupper():
        cap_letters += 1

    else:
        low_letters += 1

print(f"There are {cap_letters} captial letters in the string.")
print(f"There are {low_letters} lowercase letters in the string.")
