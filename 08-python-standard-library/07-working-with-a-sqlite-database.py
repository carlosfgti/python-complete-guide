import sqlite3
from pathlib import Path

all_courses = [
    {"id": 1, "title": "Python", "available": True},
    {"id": 2, "title": "PHP", "available": False},
]

# all_courses = json.dumps(courses)
# with sqlite3.connect("db.db") as connection:
#     command = "INSERT INTO courses (id, title, available) VALUES (?, ?, ?)"
#     for course in all_courses:
#         # print(tuple(course.values()))
#         connection.execute(command, tuple(course.values()))
#     connection.commit()

with sqlite3.connect("db.db") as connection:
    command = "SELECT * FROM courses"
    cursor = connection.execute(command)
    for row in cursor:
        print(row)