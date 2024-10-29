class Employee:
    overtime_rate = 1.5
    def __init__(self, name, emp_type, working_hours):
        self.__name = name
        self.__emp_type = emp_type
        self.__working_hours = working_hours
        self.__overtime_pay = 0

    def calculate_salary(self):
        if self.__emp_type == 'full-time':
            base_salary = 3000
            if self.__working_hours > 160:
                overtime_hours = self.__working_hours - 160
                self.__overtime_pay = overtime_hours * 20 * Employee.overtime_rate 
                total_salary = base_salary + self.__overtime_pay
                return base_salary
            return base_salary

        elif self.__emp_type == 'part-time':
            hourly_rate = 15
            if self.__working_hours > 80:
                overtime_hours = self.__working_hours - 80
                self.__overtime_pay = overtime_hours * hourly_rate * Employee.overtime_rate
                total_salary = (80 * hourly_rate) + self.__overtime_pay
                return total_salary
            return self.__working_hours * hourly_rate

        elif self.__emp_type == 'intern':
            base_salary = 500
            return base_salary
    
        else:
            print('Invalid Employee Type')
    

    def display(self):
        print(f'Name: {self.__name}, Employee Type: {self.__emp_type}, Working Hours: {self.__working_hours}, Salary: {self.calculate_salary()}, Overtime pay: {self.__overtime_pay}')

    


