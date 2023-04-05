def cal_half_age(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 2 / age

try:
    response = cal_half_age(-2)
    print(response)
except ValueError as ex:
    print(ex)
