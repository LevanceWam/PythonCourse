# reverse the following list using for loop
# by Levance Wamley jr

list1 = [1, 2, 3, 4]


def reversedList(list):
    newList = []
    for i in list1:
        newList.append(i)
    newList.reverse()
    print(newList)


reversedList(list1)

# another way
start = len(list1)-1
stop = -1
step = -1

for i in range(start, stop, step):
    print(list1[i])
