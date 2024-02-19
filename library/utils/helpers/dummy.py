import random

""" Loads dummy data to the file. File path is optional. Size is required. Before the process, it asks to User if wants to remove file or overwrite."""


class DummyData:
    def __init__(self, quantity=None):
        self.quantity = quantity
        self.letters = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
        self.grand_library = list(
            zip(
                self._generate_authors(),
                self._generate_books(),
                self._generate_release_date(),
                self._generate_num_of_pages(),
            )
        )

    def _generate_authors(self):
        authors = []
        first = ""
        last = ""
        for i in range(self.quantity):
            for i in range(random.randint(5, 10)):
                first += random.choice(self.letters)
                last += random.choice(self.letters)
            author = first.title() + " " + last.title()
            authors.append(author)
            first = ""
            last = ""
        return authors

    def _generate_books(self):
        books = []
        first = ""
        last = ""
        for i in range(self.quantity):
            for i in range(random.randint(5, 20)):
                first += random.choice(self.letters)
                last += random.choice(self.letters)
            book = first.title() + " " + last.title()
            books.append(book)
            first = ""
            last = ""
        return books

    def _generate_release_date(self):
        release_dates = []
        for i in range(self.quantity):
            release_dates.append(random.randint(1900, 2024))
        return release_dates

    def _generate_num_of_pages(self):
        pages = []
        for i in range(self.quantity):
            pages.append(random.randint(20, 2000))
        return pages

    def write_to_file(self, file):
        with open(file, "w+") as file:
            for author, book, release_date, num_of_pages in self.grand_library:
                file.write(f"{author},{book},{release_date},{num_of_pages}\n")
