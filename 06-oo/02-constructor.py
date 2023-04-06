class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("automatic")

    def introduce(self):
        print("Hi, my name is " + self.name + " and I am " + str(self.age) + " years old.")

person1 = Person("Carlos", 30)

person1.introduce()
