class Triangle:
    def __init__(self, first_angle: float, second_angle:float):
        self.first_angle = first_angle
        self.second_angle = second_angle
        self.third_angle = 0.0

    def cal_third_angle(self):
        self.third_angle = 180 - (self.first_angle + self.second_angle)

