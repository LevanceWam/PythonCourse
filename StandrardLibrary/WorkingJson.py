import json
from pathlib import Path

# writing the json file
# movies = [
#     {"id": 1, "title": "Riddick", "year": 2012},
#     {"id": 2, "title": "Terminator", "year": 1989},
#     {"id": 3, "title": "Chucky", "year": 1999}
# ]
# data = json.dumps(movies)
# Path("movies.json").write_text(data)

# Here we are reading the text from the file
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0])
