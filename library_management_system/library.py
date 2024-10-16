class Library:
    def __init__(self):
        Library.books = []
        
    def add_book(self, book ):
        Library.books.append(book)

    def display_books(self):
        print('Available Books: ')
        for book in Library.books:
            book.display()