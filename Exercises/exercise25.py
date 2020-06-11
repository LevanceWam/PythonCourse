# write a function that takes 2 variables and calculates
# addition and subtraction and returns both
# by Levance Wamley


def calculation(a, b):
    addition = a+b
    subtraction = a-b
    return addition, subtraction


result = calculation(40, 10)
print(result)


# shorter
def calculate(a, b):
    return a+b, a-b


res = calculate(20, 40)
print(res)
