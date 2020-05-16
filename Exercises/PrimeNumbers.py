# Create a Program that will give you all of the prime #'s in a list.
# By Levance,

#
start = 5
end = 17
primes = []
for num in range(start, end+1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
