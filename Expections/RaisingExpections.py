def calculate_xfactor(age):
    if age <= 0:
        # this is us giving the user an error
        raise ValueError("Age can not be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
