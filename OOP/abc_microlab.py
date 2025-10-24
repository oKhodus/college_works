from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        return pi * pow(self.radius, 2)
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def area(self):
        value = self.width * self.height
        return int(value) if value.is_integer() else value
    
c = Circle(3)
print(round(c.area(), 3))

r = Rectangle(4, 5)
print(r.area())