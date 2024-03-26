from abc import ABC

class Shape(ABC):
    @abstarctmethod
    def area(self):
        pass

    @abstarctmethod
    def perimenter(self):
        pass

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2

    def perimeter(self):
        ret
        urn 2 *()