print("Learning Inheritance in Python")

class Car:
    def __init__(self, color, capacity):
        self.color = color
        self.capacity = capacity

    def start(self):
        print("Starting this car")

    def stop(self):
        print("Stopping this car")


class Honda(Car):
    def printName(self):
        print("Honda Cars")


car = Honda("Red", 3)
car.printName()
car.start()
car.stop()