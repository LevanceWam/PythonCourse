# When python sees the try block it will run all the code in this block
# if any of the statements throws an expection the except code will run
# not it will run the code in the block
try:
    age = int(input("Age"))
except ValueError as ex:
    print("You didn't enter a valued age")
    # this will give us information about the error message
    print(ex)
    print(type(ex))
else:
    # this will run if there is no exceptions
    print("No exceptions were thrown")
# if an expection is thrown due to error this will still run
print("execution continues")
