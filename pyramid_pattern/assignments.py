line = int(input('Number of lines: '))

# No 1: Pyramid Patterns with Alphabet

for i in range(1, line+1):
    print(' ' * (line - i), end = "")
    
    num = 65

    for j in range(1,i+1):
        print(chr(num), end = " ")
        num += 1
        
    print()
 

#No 2: Pyramid Patterns with Numbers

for i in range(1, line+1):
    print(' ' * (line-i), end = "")

    for r in range(1,(i*2)):
        print(i, end = "")
    print()
    
#No 3: Inverted Half Pyramid Pattern

for i in range(line):
    print('*' * (line-i), end = "")
    print()

#No 4: Numeric Pattern

for i in range(line, 0, -1):
    for n in range(1,i+1):
        print(f'{n}'  , end = " ")
    print()

for j in range(1,line+1):
    for n in range(1,j+1):
        print(f'{n}'  , end = " ")
    print()

#No 5: Rhombus Pattern

for i in range(1,line+1):
    print(' ' * (line-i), end = "")
    print('*' * line)

#No 6: Inverted Full Pyramid Pattern

i = 1
while (i <= line):
    space = i - 1
    j = 1
    while (j <= space):
        print(' ', end = "")
        j += 1

    star = (line - i) * 2 + 1
    k = 1
    while (k <= star):
        print('*', end = "")
        k += 1
    print()
    i += 1

