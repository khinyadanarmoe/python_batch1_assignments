from triangle import Triangle

a1 = float(input('First angle: '))
a2 = float(input('Second angle: '))

triangle = Triangle(a1, a2)

triangle.cal_third_angle()

print(f'The third angle is: {triangle.third_angle}')