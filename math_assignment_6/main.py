from cylinder import Cylinder

radius = float(input('Enter Radius: '))
height = float(input('Enter Height: '))
cylinder = Cylinder(radius,height)
cylinder.surface_area()