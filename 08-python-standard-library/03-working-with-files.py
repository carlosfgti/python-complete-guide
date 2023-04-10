from pathlib import Path

path = Path("test.txt")
print(path.exists())
if not path.exists():
    path.touch()
    path.rename("test.txt")
path.unlink()