class Employee:
    overtime_rate = 1.5
    def __init__(self, name, emp_type, working_hours):
        self.name = name
        self.emp_type = emp_type
        self.working_hours = working_hours
        self.overtime_pay = 0

    def calculate_salary(self):
        if self.emp_type == 'full-time':
            base_salary = 3000
            if self.working_hours > 160:
                overtime_hours = self.working_hours - 160
                self.overtime_pay = overtime_hours * 20 * Employee.overtime_rate 
                total_salary = base_salary + self.overtime_pay
                return base_salary
            return base_salary

        elif self.emp_type == 'part-time':
            hourly_rate = 15
            if self.working_hours > 80:
                overtime_hours = self.working_hours - 80
                self.overtime_pay = overtime_hours * hourly_rate * Employee.overtime_rate
                total_salary = (80 * hourly_rate) + self.overtime_pay
                return total_salary
            return self.working_hours * hourly_rate

        elif self.emp_type == 'intern':
            base_salary = 500
            return base_salary
    
        else:
            print('Invalid Employee Type')
    

    def display(self):
        print(f'Name: {self.name}, Employee Type: {self.emp_type}, Working Hours: {self.working_hours}, Salary: {self.calculate_salary()}, Overtime pay: {self.overtime_pay}')

    


