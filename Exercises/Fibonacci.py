# Create program that follows a Fibonacci sequence.
# By Levance Wamley

# Let's create a function that can handle all of the work


def fibo(n):
    a, b = 0, 1
    # if the user types 1 just show them 0
    if n == 1:
        print(a)
    elif n < 0:
        # if the user tries to use negative numbers show this message.
        print("I'm sorry I am not able to go backwards yet.")
    else:
        print(a)
        print(b)
        for x in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
        final = c
        print(f"The final number is: {final}")


# We will allow the user to input their own number and decide how long they want the sequence to go.
question = input('Enter a Number: ')
# change the string to a integer
number = int(question)
fibo(number)
