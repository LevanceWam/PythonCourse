# create a program that takes 2 integers from user output
# then return the product
# if it the product is over 1000 return the sum instead
# By Levance Wamley jr

# accept user input and change it to integers
num = int(input('Enter First number: '))
num2 = int(input('Enter Second number: '))


def productOrSum(number, number2):
    limit = 1000  # define a limit no magic numbers
    total = number * number2

    if total >= limit:  # if the total is bigger than the limit we set add instead
        total = number + number2
        print(f'The result is: {total}')
    else:
        # if total is less than limit then just multiply
        print(f'The result is: {total}')


productOrSum(num, num2)
