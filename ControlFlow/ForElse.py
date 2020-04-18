successful = True
for number in range(3):
    print("Attempt", number)
    if successful and number >= 3:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
