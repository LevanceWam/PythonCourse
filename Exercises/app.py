# Let's write a program that will count the amount of capital letters in a file
import random
import string

file = open('sample.txt')
data = file.read()
words = data.split()
capitals = 0
lowers = 0

for word in words:
    if word.isupper():
        capitals += 1
    else:
        lowers += 1

print(f"There are {capitals} captial letters in the file.")
print(f"There are {lowers} lowercase letters in the file.")

cap_letters = 0
low_letters = 0
sentence = "".join(random.choices(string.ascii_letters, k=20))

for caps in sentence:
    if caps.isupper():
        cap_letters += 1

    else:
        low_letters += 1

print(f"There are {cap_letters} captial letters in the string.")
print(f"There are {low_letters} lowercase letters in the string.")
