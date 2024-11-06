from triangle import Triangle
a = int(input('Enter the length of side a: '))
b = int(input('Enter the length of side b: '))
c = int(input('Enter the length of side c: '))

tri = Triangle(a,b,c)
tri.cal_angles()
tri.display()