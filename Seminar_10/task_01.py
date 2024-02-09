import math


class Circle:
    pi = math.pi
    def __init__(self, radius):
        self.radius = radius

    def circle_length(self):
        return 2 * self.pi * self.radius

    def circle_area(self):
        return math.pi * self.radius ** 2


circle = Circle(3)
print(circle.circle_length())
print(circle.circle_area())