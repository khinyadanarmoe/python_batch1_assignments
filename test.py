from student import Student
students = []

def get_marks():
    marks = []
    sub_count = 1
    while True:
        mark = int(input(f'Enter Subject{sub_count} mark: '))
        marks.append(mark)
        sub_count+=1
        flag = input('Do you want to continue:Yes/No ')
        if flag != 'yes':
            break
    return marks


def get_student_info():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    get_marks()
    student = Student(name,email,address,get_marks())
    students.append(student)
    

#same as do_while
while True:
    get_student_info()
    flag = input('Do you want to continue:Yes/No ')
    if flag != 'yes':
        break

for student in students:
    student.display()