items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

items.sort(key=lambda item: item[1])
print(items)

# Lambda is basically an anonymous function
# we cab pass these to all functions
