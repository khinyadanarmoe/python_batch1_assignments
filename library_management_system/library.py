class Library:

    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"added {book.get_title()}")

    def display_books(self):
        print('Available Books: ')
        for book in self.books:
            book.display()