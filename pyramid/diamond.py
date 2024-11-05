def half_inverted_space_pyramid(line: int, i: int):
    space = i - 1
    j = 1
    while j <= space:
        print(" ", end=" ")
        j += 1

def inverted_star_pyramid(line: int, i: int):
    star = (line - i) * 2 + 1
    j = 1
    while j <= star:
        print("*", end=" ")
        j += 1

def half_space_pyramid(line: int, i: int):
    space = line - i
    j = 1
    while j <= space:
        print(" ", end=" ")
        j += 1

def star_pyramid(i: int):
    star = i * 2 + 1
    k = 1
    while k <= star:
        print("*", end=" ")
        k += 1

def inverted_full_pyramid(line):
    i = 1
    while i <= line:
        half_inverted_space_pyramid(line, i)
        inverted_star_pyramid(line, i)
        print()
        i += 1

def full_pyramid(line):
    i = 0
    while i <= line - 1:
        half_space_pyramid(line, i)
        star_pyramid(i)
        print()
        i += 1

line = int(input("Enter sandglass star pattern size: "))
half_line = line // 2

full_pyramid(half_line)
inverted_full_pyramid(half_line + 1)
