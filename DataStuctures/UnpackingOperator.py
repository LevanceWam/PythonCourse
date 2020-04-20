# the * operator will unpack any iterables
# for dictionaries you have to use **

numbers = [1, 2, 3]
print(*numbers)

values = [*range(5), *"Hello"]
print(values)

first = {"x": 1}
second = {"x": 10, "y": 20}  # since x was called last it will be prnted
combined = {**first, **second, "z": 1}
print(combined)
