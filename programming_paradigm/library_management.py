class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        #self._is_checked_out = is_checked_out
    
    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True
    
    def return_to_shelf(self):
        """Marks the book available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and marks it as checked out."""
        for book in self._books:
            # We check if the title matches AND it it is actually available
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Successfully checked out '{title}'")
                return
        print(f"Sorry, '{title}' is not available or not found.")

    def return_book(self, title):
        """Finds a book by title and marks it as returned."""
        for book in self._books:
             if book.title == title:
                book.return_to_shelf()
                print(f"Successfully returned '{title}'.")
                return
        print(f"Book '{title}' does not belong to this library.")

    
    def list_available_books(self):
        """Prints all books that are currently not checked out."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
