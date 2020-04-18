number = 100
# This will make the loop divide till it's at 0
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input("> ")
    print("ECHO", command)
