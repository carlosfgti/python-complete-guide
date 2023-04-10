from pathlib import Path

print(Path())
path = Path("01-working-with-paths.py")
print(path.is_dir())
print(path.is_file())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.with_name("errors.log"))
print(path.with_suffix(".log"))