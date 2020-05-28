# Given a list of numbers,
# return true if the first and last numbers are the same
# by Levance Wamley jr

numList = [2, 3, 4, 5, 2, 8]
numList2 = [3, 2, 4, 5, 6, 7, 8, 7, 3]


def listChecker(list):
    start = list[0]
    end = list[-1]

    result = "Result is : True" if start == end else "Result is : False"
    print(result)


listChecker(numList)
listChecker(numList2)
