# Given two list of numbers
# create a new list that will
# take the odd numbers from the first list
# take even numbers from the second list
# by Levance Wamley jr

firstList = [11, 23, 44, 67, 232, 4, 32, 21]
secondList = [22, 32, 456, 3, 45, 11, 55, 87, 98]
result = []

print('First List:', firstList)
print('Second List:', secondList)


def thirdList(list1, list2):
    for num in list1:
        if num % 2 == 1:
            result.append(num)

    for num in list2:
        if num % 2 == 0:
            result.append(num)
    print('Third List:', result)


thirdList(firstList, secondList)
