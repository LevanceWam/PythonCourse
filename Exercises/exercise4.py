# return the total count of emma appears in a string
# By Levance Wamley Jr

sentence = 'Emma is a good developer. Emma is a writer. emma emma Emma.'


def findWord(sentence, word):
    count = 0
    data = sentence.lower().replace(".", "").split()
    for item in data:
        if item == word.lower():
            count += 1

    print(count)


findWord(sentence, 'Emma')
