def sum(*numbers):
    total = 0
    for number in numbers:
        #print(number)
        total += number
    return total

print(sum(2, 4, 6, 7))