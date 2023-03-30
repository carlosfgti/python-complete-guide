def example():
    message = "example"

# error -> print(message)

message2 = "example b"
def example2():
    return message2

print(message2, example2())

print("----------------")

def example3():
    # don't recommended 
    global message2
    message2 = "updated"
    print(message2)
example3()

print(message2)