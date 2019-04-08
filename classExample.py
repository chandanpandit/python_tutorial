class Person:
    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    def walk(self):
        print("I am walking")

    def sleep(self):
        print("I am sleeping")

    def eat(self):
        print("I am eating")

    def getName(self):
        return self.name


person = Person("Chandan", 25, 5, "M")
person.walk()
print(person.getName())
print(person.age)

person2 = Person("Ram", 28, 6, "M")
print(person2.getName())
person2.sleep()