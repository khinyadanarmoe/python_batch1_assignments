import math
class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def cal_angles(self):
        rad_A = math.acos((self.side_b**2 + self.side_c **2 - self.side_a ** 2)/ ( 2 *  self.side_b * self.side_c))
        rad_B = math.acos((self.side_a**2 + self.side_c **2 - self.side_b ** 2)/ ( 2 *  self.side_a * self.side_c))
        rad_C = math.acos((self.side_a**2 + self.side_b **2 - self.side_c ** 2)/ ( 2 *  self.side_a * self.side_b))

        self.angle_A = math.degrees(rad_A)
        self.angle_B = math.degrees(rad_B)
        self.angle_C = math.degrees(rad_C)

    def display(self):
        print(f'Angles of the triangle are: {self.angle_A:.2f}, {self.angle_B:.2f} and {self.angle_C:.2f}') 