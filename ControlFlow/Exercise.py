# exercise write a program that will display the even numbers from 1 to 10
# can not use the step argument
# My attempt
count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")
# print(f"We have {x} even numbers")

# my attempt with while loops
number = 2
while number < 10:
    print(number)
    number += 2
