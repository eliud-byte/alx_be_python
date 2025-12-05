class Book:
    """Base class for all books in the library."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}"

    def get_details(self):
        """Returns basic book details."""
        return f"{self.__class__.__name__}: {self.title} by {self.author}"

class EBook(Book):
    """Represents an electronic book."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns details specific to the EBook."""
        base_details = super().get_details()
        return f"{base_details}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Represents a physical printed book."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns details specific to the PrintBook."""
        base_details = super().get_details()
        return f"{base_details}, Page Count: {self.page_count}"

class Library():
    """Manages a collection of Book, EBook, and PrintBook instances"""
    def __init__(self):
        self.books = []
    
    def add_book(self, book: Book):
        """Adds a Book, EBook, or PrintBook instance to the library's collection."""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added '{book.title}' to the library")    
        else:
            print("Error: Item is not a valid Book type.")

    def list_books(self):
        """Prints details of every book in the library."""
        print("\n--- Current Library Collection ---")
        if not self.books:
            print("The library is currently emply.")
            return
             
        for book in self.books:
            print(book)

        print("------------------------------------------------------")