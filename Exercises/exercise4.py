# return the total count of emma appears in a string
# By Levance Wamley Jr

sentence = 'Emma is a good developer. Emma is a writer. emma emma Emma.'


def findWord(sentence, word):
    count = 0
    # for data we lower cased the sentence and remove any '.'
    # this is because no matter what the user types whether its upper or lower
    # we can find the given word
    # also when ever a word is connected to a special character it over looks
    data = sentence.lower().replace(".", "").split()
    for item in data:
        if item == word.lower():
            # lowercase the word we are searching for
            count += 1

    print(count)


findWord(sentence, 'Emma')
