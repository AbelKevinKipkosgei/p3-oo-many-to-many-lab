class Author:
    all = []  # Class variable to track all authors

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def __repr__(self):
        return f"Author(name='{self.name}')"

    def contracts(self):
        # Return a list of contracts associated with this author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Return a list of books associated with this author via contracts
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # Create and return a new contract between the author and the book
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Calculate total royalties earned by the author from all contracts
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    all = []  # Class variable to track all books

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def __repr__(self):
        return f"Book(title='{self.title}')"

    def contracts(self):
        # Return a list of contracts associated with this book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Return a list of authors associated with this book via contracts
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    def __eq__(self, other):
        return (self.author == other.author and 
                self.book == other.book and 
                self.date == other.date and 
                self.royalties == other.royalties)

    def __repr__(self):
        return f"Contract(author={self.author.name}, book={self.book.title}, date={self.date}, royalties={self.royalties})"

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
