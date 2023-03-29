active = False
for number in range(10):
    print("Attempt")
    if active:
        print("Active")
        break
else:
    print("Attempted 10 times and failed")