items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = []
for item in items:
    prices.append(item[1])  # will return the price of items
print(prices)

x = map(lambda item: item[1], items)  # this is the same as the loop above this
for item in x:
    print(item)  # this will give us the price
print(x)  # this will give us the map iterable

# This is the same as the 2 loops above this
y = list(map(lambda item: item[1], items))
print(y)
