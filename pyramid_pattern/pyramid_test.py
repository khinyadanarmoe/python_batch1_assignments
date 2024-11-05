'''
for i in range(5):
    for j in range(5):
        print('*', end = "")
    print()
    

i = 1
line = 5
while i <= line:
    j = 1
    while j <= i:
        print('*', end = "")
        j += 1
    print()

    i += 1

for i in range(6,0,-1):
    for j in range(i):
        print('*', end = "")
    print()



def half_pyramid(line):
    for i in range(line + 1):
        for j in range(i):
            print('*', end = "")
        print()

line = int(input('Enter pyramid size:  '))
half_pyramid(line)

def half_pyramid_num(line):
    for i in range(line + 1):
        for j in range(1,i+1):
            print(j, end = "")
        print()

line = int(input('Enter pyramid size:  '))
half_pyramid_num(line)
'''

line = int(input('inverted pyramid size: '))
num = 65
for i in range(1,line+1):
    for j in range(i):
        ch = chr(num)
        print(ch, end = " ")
    num = num + 1
    print()
    

line = 5
for i in range(1, line+1):
    for j in range(i):
        print(" " * j , '*' * (i+2))
    print()
        
line = 5
i = 1
while i <= line:
    j = line - i
    while j >= 1:
        print(" ", end = " ")
        j = j -1 
    
    r = 1
    while r <= (i * 2)-1:
        print(r, end = " ")
        r = r + 1
    print()
    i = i + 1

for i in range (1,line+1):
    for j in range(line - i, 0, -1):
        print(" ", end = " ")
    
    for r in range(1,(i*2)):
        print(r, end = " ")
    print()