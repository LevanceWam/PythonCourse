# Given a list of numbers
# iterate through the list
# print the numbers that are divisble by 5
# if the number is greater than 150 stop the iteration
# by Levance Wamley jr

numList = [5, 10, 15, 150, 16, 29, 20, 25, 55]
for i in numList:
    if i % 5 == 0:
        print(i)
    if i == 150:
        break
