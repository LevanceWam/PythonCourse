# write a program that display a number pyramid
# by Levance Wamley jr

n = 7
for row in range(n):
    for col in range(row):
        print(col+1, end=' ')
    print()
