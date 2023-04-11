from pathlib import Path
from zipfile import ZipFile

# zip = ZipFile("files.zip", "w")
# for path in Path("08-python-standard-library").rglob("*.py"):
#     zip.write(path)
# zip.close()

with ZipFile("files.zip", "w") as zip:
    for path in Path("08-python-standard-library").rglob("*.py"):
        zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("08-python-standard-library/04-working-with-zip-files.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("tmp")

print("------------------------")
for file in Path("tmp/08-python-standard-library").rglob("*.*"):
    file.unlink()
Path("tmp/08-python-standard-library").rmdir()
Path("tmp").rmdir()
Path("files.zip").unlink()