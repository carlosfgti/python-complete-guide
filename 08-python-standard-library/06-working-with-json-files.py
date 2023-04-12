import json
from pathlib import Path

courses = [
    {"id": 1, "title": "Python", "available": True},
    {"id": 2, "title": "PHP", "available": False},
]

data = json.dumps(courses)
path = Path("courses.json")
path.write_text(data)

courses = json.loads(data)
print(courses)
path.unlink()