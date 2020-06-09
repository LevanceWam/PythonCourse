# print a number pyramid backwards

n = 5
k = 5

for row in range(0, n+1):
    for col in range(k - row, 0, -1):
        print(col, end=' ')
    print()
