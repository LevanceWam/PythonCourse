# lets get rid of the duplicates
numbers = [1, 1, 2, 4, 5, 2]
first = set(numbers)
print(first)
second = {3, 4, 6}
# Uses the same methods as list
len(second)
# sets can do some cool stuff with math
# will return a new set with all the items in both sets
print(first | second)
# will return the numbers that are the same in both sets
print(first & second)
# this will print the difference in both sets will show what is not in the second set
print(first - second)
# this will print what ever is in the sets but not in both of them (no dupiclates)
print(first ^ second)

# sets are not in sequence ,it does not support indexes
# if we need to find something we do it like this:
if 1 in first:
    print("yes")
