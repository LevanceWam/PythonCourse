def diamond(rows):
    for i in range(rows):
        # this part of the for loop deals with the top of the diamond
        print(" "*(rows-i-1)+"* "*(i+1))
    for j in range(rows-1, 0, -1):
        # this part of the loop deals with the bottom of the diamond
        print(" "*(rows-j)+"* "*(j))


diamond(4)
