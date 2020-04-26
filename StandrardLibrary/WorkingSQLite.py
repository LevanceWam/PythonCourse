import sqlite3
import json
from pathlib import Path

# Lets move the information from movies.json to SQLite database
# movies = json.loads(Path("movies.json").read_text())
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

# Now we are going to read from SQLite db
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
# We will won't be able to execute the bottom code because we are already iterating through the cursor and can't restart it. comment out the 2 lines above to run
    movies = cursor.fetchall()
    print(movies)
