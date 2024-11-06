import math
class Circle:
    def __init__(self,r: float):
        self.r = r

    def area(self):
        return math.pi * math.pow(self.r, 2)
    
    def perimeter(self):
        return 2 * math.pi * self.r
    
    def display(self):
        print(f'Area: {self.area():.2f}')
        print(f'Perimeter: {self.perimeter():.2f}')