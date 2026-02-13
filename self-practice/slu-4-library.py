class Book:
    def __init__(self, author, title, isbn):
        self.author = author.title()
        self.title = title
        self.isbn = int(isbn)

    def get_author_name(self):
        return f"{self.author} -- {self.title}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, author, title, isbn):
        b = Book(author, title, isbn)
        self.books.append(b)

    def get_book_by_isbn(self, isbn):
        target = int(isbn)
        for book in self.books:
            if book.isbn == target:
                return book
        return None
