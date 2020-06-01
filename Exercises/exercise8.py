# write a program to see if when a number is reversed it is the same as the original
# by Levance Wamley jr
num = 101
print('Original Number:', num)


def palidromeNum(num):
    if str(num) == str(num)[::-1]:
        print('The original and the reverse number are the same:', True)
    else:
        print('The original and the reverse number are the same:', False)


palidromeNum(num)
