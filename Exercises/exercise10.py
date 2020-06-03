# create a function that takes decimal numbers
# Then converts them into octal numbers
# by Levance Wamley jr


# '%o' is a string formatting for octal numbers
def decimalToOctal(n):
    fullOct = oct(n)
    halfOct = '%o' % n
    print(f'The full octal of {n} is {fullOct}')
    print(f'The octal of {n} is {halfOct}')


decimalToOctal(16)
