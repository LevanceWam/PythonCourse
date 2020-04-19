numbers = [1, 2, 3]
numbers2 = [1, 2, 3, 3, 4, 5, 4, 5, 5]
first, second, third = numbers  # this is the same as the code below
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# so what whill this do is put the first 2 items in variables and then put the rest in a list name other
fouth, fifth, * other = numbers2
print(fouth, fifth)
print(other)
sixth, *other2, last = numbers2
print(sixth, last)  # will print the first and last numbers of the list
print(other2)  # will print everything in the middle
