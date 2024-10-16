from employee import Employee

employees_db = []

def get_info():
    name = input('Enter Employee Name: ')
    emp_type = input('Enter Employee Type: ')
    working_hours = int(input('Enter Employee Working Hours: '))

    emp = Employee(name, emp_type, working_hours)
    return emp

while True:
    employee = get_info()
    employees_db.append(employee)
    flag = input('Do you want to add another employee:Yes/No')
    if flag != 'yes':
        break


for employee in employees_db:
    employee.display()