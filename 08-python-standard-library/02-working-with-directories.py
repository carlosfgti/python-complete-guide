from pathlib import Path

path = Path("images")
print(path.exists())
# print(path.mkdir())
print(path.exists())
# print(path.rmdir())
# print(path.rename("image2"))

path2 = Path("08-python-standard-library")
for result in path2.iterdir():
    print(result)

print(list(path2.glob("*.py")))