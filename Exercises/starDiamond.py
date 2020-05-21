def diamond(rows):
    # how we make the columns
    for i in range(rows):
        # this part of the for loop deals with the top of the diamond
        # We are multiplying the amount of spaces the sum of rows - the iteration - 1
        # Example 4 - 0 - 1 = 3 for the first iteration we will get 3 spaces then we get a star
        print(" "*(rows-i-1)+"* "*(i+1))
    for j in range(rows-1, 0, -1):
        # this part of the loop deals with the bottom of the diamond
        # Here we are building the triangle backwards
        # we subtracted one from the rows so it can start on a desecent from the top triangle
        # we then set the counter to zero and the step to negative one so it count backwards
        print(" "*(rows-j)+"* "*(j))
        # So this print is gonna execute the number of spaces by multiplying the difference of rows and the iteration
        # then we multipy the iteration and * to get the stars for that row


diamond(10)
