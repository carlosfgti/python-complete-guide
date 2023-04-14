import subprocess

subprocess.run(["ls", "-la"])
print("--------------")
result = subprocess.run(["npm", "--version"])
print(type(result))
print("--------------")
completed = subprocess.run(["ls"],
                           capture_output=True)
print("args", completed.args)
print("returncode", completed.returncode)
print("stderr", completed.stderr)
print("stdout", completed.stdout)