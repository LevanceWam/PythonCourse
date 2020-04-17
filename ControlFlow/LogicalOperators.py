# and: both statements are true then code will run
# or: One of the statements has to be correct to run
# not: Inverse the value of a boolean

high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
