letters = ["a", "b", "c", "e", "f", "h", "g"]

# Add
letters.append("d")  # adds to the end
letters.insert(0, "-")  # adds at a specific spot
print(letters)

# Remove
letters.pop()  # removes the last item in the list
letters.pop(0)  # Removes a item from a specific spot
# will search through the list till the item called is found
letters.remove("b")
del letters[0:3]  # deletes a range of numbers
letters.clear()  # deletes the whole list
print()
