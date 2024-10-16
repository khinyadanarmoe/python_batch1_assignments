class Book:
    def __init__(self, title: str, author: str, isbn: str, available_copies: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def borrow(self):
        if (self.available_copies > 0):
            self.available_copies -= 1
            print(f'Borrowed: {self.title}. Available copies: {self.available_copies}')
        
        else:
            print('No copies are currently available for borrow.')

    def return_book(self):
        self.available_copies += 1
        print(f'Returned: {self.title}. Available copies: {self.available_copies}')

    def display(self):
        print(f'Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available Copies: {self.available_copies}')

