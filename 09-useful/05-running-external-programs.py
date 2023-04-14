import subprocess

subprocess.run(["ls", "-la"])
print("--------------")
result = subprocess.run(["npm", "--version"])
print(type(result))