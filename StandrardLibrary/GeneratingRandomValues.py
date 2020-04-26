import random
import string

# Gives us a random number(float) between 0 & 1
print(random.random())
# Gives us a random number between 2 selected numbers
print(random.randint(1, 10))
# Gives us a random number from out of a list
print(random.choice([1, 2, 3, 4, 5, 6]))
# Gives us 2 random numbers out of a list
print(random.choices([1, 2, 3, 4, 5, 6, 7], k=2))
print("".join(random.choices("abcdefghij", k=4)))
# returns a string with all the letters upper and lower case
print(string.ascii_letters)
# prints a string from 1 - 9
print(string.digits)
print("".join(random.choices(string.ascii_letters + string.digits, k=7)))

numbers = [1, 2, 3, 4, 5, 6]
# shuffles the array
random.shuffle(numbers)
print(numbers)
