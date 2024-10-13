#1.Calculate Rectangle Area
width = int(input('Enter width: '))
height = int(input('Enter height: '))
rectangle_area = width * height
print('The area of rectangle: ' , rectangle_area)

#2.Calculate Triangle Area
base = int(input('Enter base: '))
height = int(input('Enter height: '))
triangle_area = 1/2 * base * height
print('The area of triangle: ' , triangle_area)

#3.Calculate Circle Area
radius = float(input('Enter radius: '))
circle_area = 3.14 * (radius ** 2)
print('The area of circle: ' , circle_area)

#4. Calculate average score 
score = 0
for i in range(1,6):
    score += float(input(f'Enter score for subject{i}: '))

average = score / 5

print(f'The average score of this student is {average}')

if average < 50:
    print('Fail.')
else:
    print('Pass!')