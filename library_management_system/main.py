from library import Library
from book import Book

library = Library()
book_1 = Book('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 3)
book_2 = Book('1984','George Orwell','9780451524935',2)
library.add_book(book_1)
library.add_book(book_2)

library.display_books()

book_1.borrow()
book_2.return_book()

