class Book:
    def __init__(self, name):
        self.name = name
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def issue_book(self, name):
        for book in self.books:
            if book.name == name and book.available:
                book.available = False
                print("Book issued successfully!")
                return

        print("Book not available!")

    def return_book(self, name):
        for book in self.books:
            if book.name == name and not book.available:
                book.available = True
                print("Book returned successfully!")
                return

        print("Invalid return!")

    def display(self):
        for book in self.books:
            print(book.name, "-", 
                  "Available" if book.available else "Issued")


library = Library()

library.add_book(Book("Python"))
library.add_book(Book("Java"))

library.issue_book("Python")
library.display()

library.return_book("Python")
library.display()
