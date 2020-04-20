values = []
for x in range(5):
    values.append(x * 2)

# [expression for item in items]
# this is the same as the code above
# by adding the x in front we made it a dictionary
values2 = {x: x * 2 for x in range(5)}
print(values2)
