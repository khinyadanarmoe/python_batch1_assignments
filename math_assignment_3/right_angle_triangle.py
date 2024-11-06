import math
class RightAngledTriangle:
    def __init__(self, base:float, height:float):
        self.base = base
        self.height = height
        
    def cal_hypotenuse(self):
        base_sq = math.pow(self.base, 2)
        height_sq = math.pow(self.height,2)
        hypotenuse = math.sqrt(base_sq+height_sq)

        print(f'The hypotenuse is: {hypotenuse:.2f} units.')

