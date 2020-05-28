# create a program that takes 2 integers from user output
# then return the product
# if it the product is over 1000 return the sum instead
# By Levance Wamley jr

num = int(input('Enter First number: '))
num2 = int(input('Enter Second number: '))


def productOrSum(number, number2):
    limit = 1000
    total = number * number2

    if total >= limit:
        total = number + number2
        print(f'The result is: {total}')
    else:
        print(f'The result is: {total}')


productOrSum(num, num2)
