class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

class Library():
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out:
                    book.is_checked_out = True
                #     # print("check out successful")
                # else:
                #     print(f"{book.title} has been checked out")
                return
        # print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_checked_out:
                    book.is_checked_out = False
                #     print("book return successful")
                # else:
                #     print(f"{book.title} already in Library")
                return
        # print(f"Book titled '{title}' is not from the library.")


    def list_available_books(self):
        for book in self._books:
            if book.is_checked_out == False:
                print(f"{book.title} by {book.author}")
