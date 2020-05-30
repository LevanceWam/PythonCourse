# given a string and a integer
# remove characters from a string
# starting from 0 to n and return the new string
# by Levance Wamley jr

string = 'Vance'


def removeChar(string, n):
    length = len(string)
    if n > length:
        print('Sorry longer than the  string')
    else:
        print(string[n:])


removeChar(string, 4)
