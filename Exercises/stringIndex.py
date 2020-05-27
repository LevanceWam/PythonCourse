# create a program that will accept a string and display
# the characters that have a positive index number
# By Levance Wamley


def stringIndex(string):
    print(f'This is the original word: {string}')
    for index, letter in enumerate(string):
        if index % 2 == 0:
            print(f'Index [{index}] {letter}')


stringIndex('Levanceet')
