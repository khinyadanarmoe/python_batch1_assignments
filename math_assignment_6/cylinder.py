import math

class Cylinder:
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def surface_area(self):
        area = 2 * math.pi * self.radius * (self.radius + self.height)
        print(f'Surface Area: {area:.2f}')