# create a program that will make a star triangle
# by Levance Wamley jr

# we are setting the amount of rows we want to have
rows = 8
# This is the for loop that controls the rowss being made.


def triangle(rows):
    for x in range(0, rows):
        # So here we are making the columns this
        # Depending on which iteration it is on it will add the appropriate amount of spaces
        # Example 6 - 0 - 1 will give use 5 spaces and 1 star
        for y in range(0, rows-x-1):
            print(end=" ")
            # With this loop we will print the star then a space to seperate them
            # Depending on the iteration we will get a amount of stars
        for y in range(0, x+1):
            print("*", end=" ")
            # the print at the end is being used to create a break or new line
        print()


def reverseTriangle(rows):
    for i in range(rows, 0, -1):
        print(" "*(rows-i)+"* "*(i))


def leftTopTriangle(rows):
    for i in range(rows, 0, -1):
        print("* " * i)


def nintyDegree(rows):
    for i in range(rows+1):
        print('* ' * i)


# def rightTopTriangle(rows):
#     for i in range(0, rows):
#         for col in range(0, rows):

#             # leftTopAngleTriangle(rows)
#             # nintyDegree(rows)


def mixedTriangle():
    leftTopTriangle(rows)
    nintyDegree(rows)


# rightTopTriangle(rows)
