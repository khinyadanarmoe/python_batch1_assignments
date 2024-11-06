from quadratic_equation import QuadraticEquation

coe = list(map(int, input("Enter coefficients a, b, c: ").split()))

a = coe[0]
b = coe[1]
c = coe[2]

q1 = QuadraticEquation(a,b,c)
q1.cal_quadratics()