angles_sum = 180

def calculate_third_angle(a, b):
    c = angles_sum - (a + b)
    print(f'The third angle is {c}') 

a1 = int(input('First angle = '))
a2 = int(input('Second angle = '))
calculate_third_angle(a1, a2)
