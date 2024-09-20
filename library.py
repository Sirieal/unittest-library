class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.is_borrowed = False

    def __repr__(self):
        return f"<Book: {self.title}, {self.author} ({self.year})>"

class LibraryUser:
    def __init__(self, name):
        self.name = name
        self.borrowed_items = []

    def borrow(self, book):
        if book.is_borrowed:
            raise Exception(f"The book '{book.title}' is already borrowed.")
        book.is_borrowed = True
        self.borrowed_items.append(book)

    def return_item(self, book):
        if book not in self.borrowed_items:
            raise Exception(f"The book '{book.title}' was not borrowed by this user.")
        book.is_borrowed = False
        self.borrowed_items.remove(book)

    def __repr__(self):
        return f"<LibraryUser: {self.name}>"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

    def __repr__(self):
        return f"<Library: {len(self.books)} books>"
