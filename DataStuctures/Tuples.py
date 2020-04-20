# A read only list
# can not be changed
# we use parenthesis
# if we don't use () python will know its a tuple but it needs a trailing ","
point = 1, 2
print(type(point))
# Empty tuple
point1 = ()
# concatinating tuples
point2 = (1, 2) + (3, 4)
print(point2)
# repeat tuples
point3 = (1, 2) * 3
print(point3)
# we can convert to tuples
point4 = tuple("Hello World")
print(point4)

point5 = (1, 2, 3)
print(point5[0:2])
# unpacking
x, y, z = point5
# Check to see if an item is in the tuple
if 10 in point5:
    print("exist")
