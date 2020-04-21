try:
    age = int(input("Age: "))
    xfactor = 10 / age
# By adding () we can do multiple expections for a line and seperate them by ","
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No expecptions were thrown")
