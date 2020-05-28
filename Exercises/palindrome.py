# Create a program that checks to see if a string is palindrome
# By Levance Wamley jr


def palidrome(word):
    # store the string and remove any spaces and special chars.
    # note: I know that nesting replaces is not the prettiest but will come back to fix it.
    original = word.lower().replace(" ", "").replace(
        "'", "").replace(",", "").replace("?", "")
    # We are gonna reverse the string here.
    reverse = original[::-1]
    # The if statement goes as follows:
    # The first statement will check to see if the string is empty
    # the second part will compare if the original and the reverse are the same
    # Finally if the two variables don't match we tell them it doesn't work
    if not word:
        print("Do not leave this blank")
    elif original == reverse:
        print("Yes the word is palidrome")
    else:
        print("Sorry this word is not a Palidrome")


text = input("Enter a palindrome word or sentence.")
palidrome(text)
