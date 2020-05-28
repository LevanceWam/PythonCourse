# Create a program that will sort a numerical Datasheet
# By Levance Wamley jr

my_list = [45, 22, 11, 46, 7, 4, 67, 9]
# The code below is ment to iterate till the biggest number is at the end
# we are gonna heve the outer loop execute that code the same number of times till the whole list is sorted correctly
for j in range(len(my_list)-1):
    # here we want to tell how many times the loop will be executed
    # so from index 0 all the way to the last index
    # so because we have 8 numbers in this list it will go through the list 7 times
    for i in range(len(my_list)-1):
        # we will check each of the numbers in the list to see which number is greater
        if my_list[i] > my_list[i+1]:
            # here we are swapping the numbers if it is greater so the lower numbers can go to the front
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print("List sorted: ", my_list)
