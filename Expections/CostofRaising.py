from timeit import timeit
# we can calculate the time it take to execute code

# when writing your own functions prefer not raise your own expections

code1 = '''
def calculate_xfactor(age):
    if age <= 0:
        # this is us giving the user an error
        raise ValueError("Age can not be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
'''

code2 = '''
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age



xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
'''
# pass doesn't do anything
# can not have empty expect
print("first code: ", timeit(code1, number=10000))
# the second is faster by 4 times
print("second code: ", timeit(code2, number=10000))
