# create an inner function to calculate the following way
# create a outer function that will accept two parameters a and b
# create an inner function that will calculate the addition of a and b
# at last an outer function will add 5 into the addition and return
# by Levance Wamley jr


def outerFunction(a, b):
    def innerFunction():
        value = a + b
        return value
    newValue = innerFunction()
    print(newValue + 5)


outerFunction(2, 2)
