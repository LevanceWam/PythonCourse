import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
print(type(questions[0]))
# we get a dictionary which 2 key value pairs
print(questions[0].attrs)
print(questions[0].get("id", 0))
print(questions[0].select(".question-hyperlink"))
print(questions[0].select_one(".question-hyperlink"))
for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
