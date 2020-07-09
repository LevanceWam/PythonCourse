# bubble sort is one of the many sorting algoritms that come up in
# coding interviews all of the time
# this example is with mosh (Youtube)
# this example is probably in the data structures and algorithms course
# just checked it is will be visiting this again in the future

# these days many companies are ask data structure and algothrin questions
# in the interview to see if we can thing like a programmer

# lets look at a simple way to do bubble sort
# this code was typed along with java so this is good practice on converting code

# bubble sort is one of the simplest sorting algorithms

numbers = [5, 2, 1, 7, 9, 0, 4]


def bubbleSort(array):
    # in python I need to remember that the way I implement this program that range returns a sequence of numbers starting from 0
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            # so here we are targeting the first element because list indexes start at 0 so j is at 0 and then for the number we compare it against we add 1 to it
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]


bubbleSort(numbers)
print(numbers)
