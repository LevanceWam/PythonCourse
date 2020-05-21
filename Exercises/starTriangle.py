# create a program that will make a star triangle
# by Levance Wamley

# we are setting the amount of rows we want to have
row = 8
# This is the for loop that controls the rows being made.


def triangle(row):
    for x in range(0, row):
        # So here we are making the columns this
        # Depending on which iteration it is on it will add the appropriate amount of spaces
        # Example 6 - 0 - 1 will give use 5 spaces and 1 star
        for y in range(0, row-x-1):
            print(end=" ")
            # With this loop we will print the star then a space to seperate them
            # Depending on the iteration we will get a amount of stars
        for y in range(0, x+1):
            print("*", end=" ")
            # the print at the end is being used to create a break or new line
        print()


def reverseTriangle(row):
    for i in range(row, 0, -1):
        print(" "*(row-i)+"* "*(i))


def leftTopAngleTriangle(row):
    for i in range(row, 0, -1):
        print("* " * i)


def nintyDegree(row):
    for i in range(row+1):
        print('* ' * i)


# leftTopAngleTriangle(row)
# nintyDegree(row)

def mixedTriangle():
    leftTopAngleTriangle(row)
    nintyDegree(row)


mixedTriangle()
