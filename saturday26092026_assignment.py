class book:
    def __init__(self, bookName: str):
        self.bookName = bookName


class library:
    def __init__(self, libraryName: str):
        self.libraryName = libraryName
        self.inventory = {}
        self.borrowed_books = {}

    def add_book(self, bookN: book, NoOfCopies: int):
        if NoOfCopies <= 0:
            print("Please enter the valid value")
        else:
            if bookN.bookName in self.inventory:
                self.inventory[bookN.bookName] += NoOfCopies
            else:
                self.inventory[bookN.bookName] = NoOfCopies
                self.borrowed_books[bookN.bookName] = []

    def show_book(self):
        if not self.inventory:
            print("Empty library")
            return

        for book, count in self.inventory.items():
            print(book, "  ", count)

    def borrow_book(self, bookN: book, borrowerName: str):
        if bookN.bookName in self.inventory:

            if bookN.bookName in self.borrowed_books:
                if borrowerName in self.borrowed_books[bookN.bookName]:
                    print(
                        f"Borrowing failed: {borrowerName} "
                        f"already has book with title {bookN.bookName}"
                    )
                    return

            available_copies = self.inventory[bookN.bookName]

            if available_copies > 0:
               self.inventory[bookN.bookName] -= 1
               self.borrowed_books[bookN.bookName].append(borrowerName)
               print(f"Successfully borrowed {bookN.bookName} and copies{available_copies}")

            else:
                print("No copies available")

        else:
            print("No Copies available")


l1 = library("takshila")

b1 = book("the hidden hindu")
b2 = book("Harry Potter")

l1.add_book(b1, 3)
l1.show_book()

l1.borrow_book(b2, "tarun")
l1.borrow_book(b1, "tarun")
l1.borrow_book(b1, "eklavya")
l1.borrow_book(b1, "eklavya")
l1.borrow_book(b1, "raj")
l1.borrow_book(b1, "raj")
l1.borrow_book(b1,"tc")