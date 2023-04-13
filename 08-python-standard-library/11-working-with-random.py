import random
import string

print(random.random())
print(random.randint(1, 100))
print(random.choice([2, 4, 6, 8]))
print(random.choices([2, 4, 6, 8], k=2))
password = "".join(random.choices("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz", k=6))
print("random password:", password)
print(string.ascii_letters)
print(string.digits)
password = "".join(random.choices(string.ascii_letters + string.digits, k=12))
print("(2) random password:", password)

numbers = [1, 2, 3, 4, 5, 6]
random.shuffle(numbers)
print(numbers)
