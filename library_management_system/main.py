from library import Library
from book import Book

book1 = Book('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 3)
book2 = Book('1984','George Orwell','9780451524935',2)
book3 = Book('Java Black Book','Min Min','9780451524935',6)
book4 = Book('DataBaseManagement System', 'Aung Aung', '23343555', 10)


library1 = Library()
library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)
library1.add_book(book4)

'''
library  = Library()
book_1 = Book('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 3)
book_2 = Book('1984','George Orwell','9780451524935',2)
Library.add_book(library,book_1)
Library.add_book(library,book_2)

library.display_books()

book_1.borrow()
Book.return_book(book_2)

Book.borrow(book_1)
book_1.display()
'''

def display_menu():

    print("<<<<Library Management System>>>>")
    print("(1) Borrow Book.")
    print("(2) Return Book.")
    print("(3) Display Book.")
    print("(4) Exit.")
    menu_id = input("Please Enter Menu Id: ")
    return menu_id

def handle_menu_choice(menu_id, library):
    if menu_id == '1':
        borrow_book(library)

    elif menu_id == '2':
        return_book(library)

    elif menu_id == '3':
        display_books(library)

    elif menu_id == '4':
        exit

    else:
        print('Invalid menu choice.')

def display_books(library):
    print('<<Avaliable Books>>')
    for book in library.books:
        book.display()

def find_book_by_title(library, title):
    for book in library.books:
        if book.get_title() == title:
            return book    
    return None

def borrow_book(library):
    display_books(library)

    title = input("Enter Book Title: ")
    book = find_book_by_title(library, title)
    if book:
        book.borrow()
    else:
        print(f"Book title {book.get_title()} not found.")


def return_book(library):
    title = input('Enter Book Title: ')
    book = find_book_by_title(library, title)
    if book:
        book.return_book()
    else:
        print(f"Book title {title} not found.")


if __name__ == "__main__":

    while True:
       menu_id = display_menu()
       handle_menu_choice(menu_id, library1) 
       if menu_id == '4':
           break



