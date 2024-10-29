class Student:
    count = 0
    def __init__(self, name, email, address, marks):
        self.name = name
        self.email = email
        self.address = address
        self.marks = marks
        avg = sum(self.marks) / len(self.marks)
        Student.count += 1

    def check_pass_fail(self):
        if self.avg >= 50:
            return "Pass"
        else:
            return "Fail"

    def display(self):
        print(f'count: {Student.count} name: {self.name} email: {self.email} address: {self.address} avg: {self.avg} Exam result: {self.check_pass_fail}')


