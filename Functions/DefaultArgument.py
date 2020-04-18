# If we define a parameter and decide to leave the agrument below empty the function will still excute
def increment(number, by=5):
    return number + by

print(increment(2))
