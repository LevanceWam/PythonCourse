# Accept a list of 5 float numbers
# as a input from user
# by Levance Wamley jr

floatNumbers = []
listSize = int(input('Size of list: '))


def MakeList(size):
    if size == 0:
        return print('Sorry has to be more than 0')
    for i in range(0, size):
        n = float(input(f'Enter a number for index spot {i}: '))
        items = n
        floatNumbers.append(items)


MakeList(listSize)
print(floatNumbers)
