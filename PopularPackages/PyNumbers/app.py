import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])  # now we have a matrix
print(array)
print(type(array))
# this returns a tuple that specifies the number of items in each array
print(array.shape)
# this will give us a matrix defined by the agruments
array2 = np.zeros((3, 4), dtype=int)  # all 0s
array2 = np.ones((3, 4), dtype=int)  # all 1s
array2 = np.full((3, 4), 5, dtype=int)  # this makes the numbers 4
array2 = np.random.random((3, 4))  # this works not sure why it says it doesn't
print(array2)
print(array2[0, 0])
# Goes through the array and tells us which of the items is greater than 0.2
print(array2 > 0.2)
# creates a new array that only has the numbers greater than 0.2
print(array2[array2 > 0.2])
print(np.sum(array2))  # gives us the sum of all the numbers in the array
print(np.floor(array2))
print(np.ceil(array2))
print(np.round(array2))

first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first + second)
print(first + 2)

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)
