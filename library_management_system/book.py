class Book:
    def __init__(self, title: str, author: str, isbn: str, available_copies: int):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available_copies = available_copies

    '''
    @staticmethod
    def borrow(book):
        if (book.available_copies > 0):
            book.available_copies -= 1
            print(f'Borrowed: {book.title}. Available copies: {book.available_copies}')
        
        else:
            print('No copies are currently available for borrow.')

    @staticmethod
    def return_book(book):
        book.available_copies += 1
        print(f'Returned: {book.title}. Available copies: {book.available_copies}')
    '''

    def borrow(self):
        if (self.__available_copies > 0):
            self.__available_copies -= 1
            print(f'Borrowed: {self.__title}. Available copies: {self.__available_copies}')
        
        else:
            print('No copies are currently available for borrow.')

    def return_book(self):
        self.__available_copies += 1
        print(f'Returned: {self.__title}. Available copies: {self.__available_copies}')

    def display(self):
        print(f'Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Available Copies: {self.__available_copies}')

    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_available_copies(self):
        return self.__available_copies

