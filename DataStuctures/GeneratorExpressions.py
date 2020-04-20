from sys import getsizeof
# note that we are using ()
values = (x * 2 for x in range(10))
for x in values:
    print(x)
# generator objects are iterable
# in each iteration gives a new value
# unlike list they don't store the information in memory
# get the size of the generator object
# this takes less memory than a list
values2 = (x * 2 for x in range(100000))
print("gen:", getsizeof(values2))
