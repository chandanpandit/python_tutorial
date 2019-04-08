print("Learning Polymorphism in Python")

class Shape:
    def area(self):
        print("Shape Area")


class Rectangle(Shape):
    def __init__(self, len, br):
        self.length = len
        self.breadth = br

    def area(self):
        result = self.length * self.breadth
        print("Area = "+ str(result))


class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        result = self.base * self.height / 2
        print("Area = "+str(result))


rectangle = Rectangle(10, 5)
rectangle.area()

triangle = Triangle(10, 5)
triangle.area()