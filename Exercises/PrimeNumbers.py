# Create a Program that will give you all of the prime #'s in a list.
# By Levance,

# First we will define a start and end for the program to check.
start = 5
end = 25
# We create a for loop to iterate through the numbers defined.
# we add a one to the end so that number will show.
for num in range(start, end+1):
    # We add a 2nd loop in this loop well will take each number and divide indiviually.
    # We start at 2 be we know that prime numbers are made of just 1 and it self.
    # so if the numbers between get it to 0 then we know its not a prime.
    # if the number gets to zero we know it is not a prime then we break the loop aand go to the next number.
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
