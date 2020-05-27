# Write a program that given the range will iterate from start to finish
# Showing the current number , previous number and the sum of the two.
# By Levance Wamley


def sum(limit):
    current = 0
    for i in range(limit):
        previous = current
        current = i
        total = current + previous
        print(f'Current Number: {current} Previous Number: {previous}')
        print(f'Sum: {total}')


sum(20)
