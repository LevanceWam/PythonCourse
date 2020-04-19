numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)  # will make it go in reverse
print(sorted(numbers))  # returns a new list from the one we made

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
items.sort()
print(items)  # The items will not because python doesnt know how to sort this list


def sort_item(item):  # the function will take the tuple and it will return a value for sorting
    return item[1]  # this will take the item and return the price


items.sort(key=sort_item)  # the key is here to specify our argument
print(items)
