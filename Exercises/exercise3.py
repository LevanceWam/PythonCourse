# Given a list of numbers
# iterate through the list
# print the numbers that are divisble by 5
# by Levance Wamley jr


numList = [10, 23, 65, 50, 34, 78, 32, 68, 90, 100]


def divideList(list):
    print('Given list is:', list)
    print('Divisible of 5 in a list')
    for number in list:
        if number % 5 == 0:
            print(number)


divideList(numList)
