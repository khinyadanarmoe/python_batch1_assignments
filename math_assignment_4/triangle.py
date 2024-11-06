import math
class Triangle:
    def __init__(self, given_angle:float):
        self.given_angle = given_angle

    def cal_angle_w(self):
        w = (180 - self.given_angle) / 2
        print(f'The value of the angle w is {w} degree.')
        
    