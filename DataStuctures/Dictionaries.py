# A collection of key values pairs
# we use it to map a key to a value
# A cellphone full of contacts is an example, we map a person's name to contact details
# items in the dictionary can not be called by index [0]
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
# how to change a item in the dictionary
point["x"] = 10
print(["x"])
# How to add an item to the dictionary
point["z"] = 20
print(point["x"])
# How to check for the existence of the key
if "a" in point:
    print(point["a"])
# this will check and see if the key is there if not it will add
print(point.get("a", 0))
# how to delete a key
del point["x"]
print(point)
# how to loop over a dictionary
# this way we are print the value of the key with it
for key in point:
    print(key, point[key])
# second way to loop over dictionaries
# this way we will get a tuple and we can unpack them
for key, value in point.items():
    print(key, value)
# this will give us the same value as the one above
