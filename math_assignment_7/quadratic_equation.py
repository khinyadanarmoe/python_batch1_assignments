import math
class QuadraticEquation:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def cal_quadratics(self):
        b_sq = math.pow(self.b,2)
        cal_sqrt = b_sq - (4*self.a*self.c)
        
        solution_1 = (-self.b + math.sqrt(cal_sqrt)) / (2 * self.a)
        solution_2 = (-self.b - math.sqrt(cal_sqrt)) / (2 * self.a)

        print(f'The solutions are: x1 = {solution_1}, x2 = {solution_2}') 




