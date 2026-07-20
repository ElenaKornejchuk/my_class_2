class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [
            book for book in self.books
            if book.title != title
        ]

    def get_all_books(self):
        return [book.title for book in self.books]

    def get_total_pages(self):
        return sum(book.pages for book in self.books)

    def clear(self):
        self.books = []