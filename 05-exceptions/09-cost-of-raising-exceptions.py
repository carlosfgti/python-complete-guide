from timeit import timeit

my_code = """
def cal_half_age(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 2 / age

try:
    response = cal_half_age(-2)
    print(response)
except ValueError as ex:
    print(ex)
"""

my_code_pass = """
def cal_half_age(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 2 / age

try:
    response = cal_half_age(-2)
    print(response)
except ValueError as ex:
    pass
"""

print("Running in => ", timeit(my_code, number=1000))
print("Running in => ", timeit(my_code_pass, number=1000))
