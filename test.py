import unittest
from library import LibraryUser, Book, Library

class TestLibrary(unittest.TestCase):
    
    # Test for creating a new user
    def test_new_created_user(self):
        user = LibraryUser("Kalle")
        self.assertEqual(user.name, "Kalle")
        self.assertEqual(user.borrowed_items, [])
    
    # Test for borrowing an item
    def test_borrow_item(self):
        user = LibraryUser("Kalle")
        book = Book("Python Programming", "John Doe", 2021, 102)
        user.borrow(book)
        self.assertEqual(user.borrowed_items, [book])
        self.assertTrue(book.is_borrowed)

    # Test for returning an item
    def test_return_item(self):
        user = LibraryUser("Kalle")
        book = Book("Python Programming", "John Doe", 2021, 102)
        user.borrow(book)
        user.return_item(book)
        self.assertEqual(user.borrowed_items, [])
        self.assertFalse(book.is_borrowed)

    # Test for borrowing an item twice
    def test_borrow_item_twice(self):
        user = LibraryUser("Kalle")
        book = Book("Python Programming", "John Doe", 2021, 102)
        user.borrow(book)
        with self.assertRaises(Exception):  # Expect an exception to be raised
            user.borrow(book)

    # Test for returning an item that wasn't borrowed
    def test_return_non_borrowed_item(self):
        user = LibraryUser("Kalle")
        book = Book("Python Programming", "John Doe", 2021, 102)
        with self.assertRaises(Exception):  # Expect an exception to be raised
            user.return_item(book)

    # Test for creating a new book
    def test_create_new_book(self):
        book = Book("Learn C++", "Jane Smith", 2019, 105)
        self.assertEqual(book.title, "Learn C++")
        self.assertEqual(book.author, "Jane Smith")
        self.assertEqual(book.year, 2019)
        self.assertEqual(book.pages, 105)
        self.assertFalse(book.is_borrowed)

    # Test for borrowing and returning multiple books
    def test_borrow_multiple_books(self):
        user = LibraryUser("Kalle")
        book1 = Book("Python Programming", "John Doe", 2021, 102)
        book2 = Book("Machine Learning", "Alice Green", 2020, 300)
        
        user.borrow(book1)
        user.borrow(book2)
        
        self.assertEqual(user.borrowed_items, [book1, book2])
        self.assertTrue(book1.is_borrowed)
        self.assertTrue(book2.is_borrowed)

        # Returning books one by one
        user.return_item(book1)
        self.assertEqual(user.borrowed_items, [book2])
        self.assertFalse(book1.is_borrowed)

        user.return_item(book2)
        self.assertEqual(user.borrowed_items, [])
        self.assertFalse(book2.is_borrowed)

    # Test for borrowing a book already borrowed by someone else
    def test_borrow_book_already_borrowed(self):
        user1 = LibraryUser("Kalle")
        user2 = LibraryUser("Lisa")
        book = Book("Python Programming", "John Doe", 2021, 102)
        
        user1.borrow(book)
        with self.assertRaises(Exception):  # Expect an exception to be raised
            user2.borrow(book)

if __name__ == '__main__':
    unittest.main()
