class Borrower:
    """Represents a person who can borrow books."""

    new_id_code = 1  # Class variable

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.id = Borrower.new_id_code
        Borrower.new_id_code += 1  # Updates for next new borrower...
        self.books_borrowed = []

    def show_borrower_details(self):
        print("{:s} {:s} id: {:d}". format(self.firstname, self.lastname, self.id))

    def show_all_books(self):
        for x in self.books_borrowed:
            print("Title: {:s}". format(x))

class Book:
    """A class to represent a book in a library."""
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

class Library:
    """A class to represent a lending library."""
    def __init__(self):
        self.all_book = []
        self.all_borrower = []
    def add_book(self, book):
        self.all_book.append(book)

    def add_borrower(self, borrower):
        self.all_borrower.append(borrower.firstname + " " + borrower.lastname)

    def lend_book(self, borrower, book):
        if book in self.all_book:
            borrower.books_borrowed.append(book.name)
            self.all_book.remove(book)
            print("Lending book {:s} to {:s} {:s}". format(book.name, borrower.firstname, borrower.lastname))
        else:
            print("Sorry that's already on loan.")


def main():
    # Create some books...
    book1 = Book('Kafkas Motorbike', 'Bridget Jones', 1290)
    book2 = Book('Cooking with Custard', 'Jello Biafra', 1002)
    book3 = Book('History of Bagpipes', 'John Cairncross', 987)

    # Put the books in the library
    library = Library()  # Creates the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Create some borrowers...
    bor1 = Borrower('Kevin', 'Wilson')
    bor2 = Borrower('Rita', 'Shapiro')
    bor3 = Borrower('Max', 'Normal')

    library.add_borrower(bor1)
    library.add_borrower(bor2)
    library.add_borrower(bor3)

    # Make some loans...
    library.lend_book(bor1, book1)
    bor1.show_borrower_details()
    bor1.show_all_books()
    library.lend_book(bor2, book3)
    bor2.show_borrower_details()
    bor2.show_all_books()
    # Try to lend book3 out again...
    library.lend_book(bor3, book3)

if __name__ == "__main__":
    main()
