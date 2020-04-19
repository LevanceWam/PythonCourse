letters = ["a", "b", "c"]
# this will give us a tuple will give us the index of the item
# by us adding the index we are unpacking the items and their index
# this way it is not a tuple
for index, letter in enumerate(letters):
    print(index, letter)
