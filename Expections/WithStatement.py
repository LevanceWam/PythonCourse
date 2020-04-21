try:
    with open("Cleaningup.py") as file:
        # The with statement closes the file for us we dont need finally
        print("File opened")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No expecptions were thrown")
