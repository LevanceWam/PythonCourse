# Exercise Create program that generates fizz buzz with these rules
# If the number is divisible by 3 print fizz
# If the number is divisible by 5 print buzz
# If the number is divisible by 3 and 5 print fizz buzz
# if the number is any thing else echo the number
# my attempt


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    if input % 5 == 0:
        return "buzz"
    if input % 3 == 0:
        return "fizz"
    return f"echo {input}"


print(fizz_buzz(30))
# My attempt was correct shortened it according to the video to make look cleaner and readable
