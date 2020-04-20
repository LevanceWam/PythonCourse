letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0:3])  # returns a new list with the first 3 items in the list
# will still return the first 3 in the list will assume to start at 0
print(letters[:3])
print(letters[0:])  # Will print the whole list
print(letters[:])  # will make a copy of the original list
# list version of step will print every second or third item
print(letters[::2])
numbers = list(range(20))
print(numbers[::2])  # With this we will get all the even numbers
print(numbers[::-1])  # we get a list that prints backwards from 20
