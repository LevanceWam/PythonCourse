items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = list(map(lambda item: item[1], items))
prices1 = [item[1] for item in items]  # this is the same as line 7

filtered = list(filter(lambda item: item[1] >= 10, items))
# this is the same as line 10
filtered1 = [item for item in items if item[1] >= 10]
