# Q1: Vad är en instans?

# Q2: Vad är self i en klass? Varför används det?

# Q3: Vad är attributes, instance variables och methods?


class Book:
    def __init__(self, author, title, isbn):
        self.author = author.title() # str.title() capitalizes the first letter of each word
        self.title = title
        self.isbn = int(isbn)

    def get_author_name(self):
        return f"{self.author} -- {self.title}"

# Testing Book class
book_a = Book("J.R.R. Tolkien", "The Lord of the Rings", 9780544003415)
book_b = Book("J.K. Rowling", "Harry Potter and the Sorcerer's Stone", 9780439708180)
book_c = Book("George Orwell", "1984", 9780451524935)


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

# Testing Library class
lib = Library()
lib.add_book("Mary Shelley", "Frankenstein", 9780486282114)
lib.add_book("H.G. Wells", "The War of the Worlds", 9780451530653)
lib.add_book("Bram Stoker", "Dracula", 9780486411095)