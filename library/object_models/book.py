from dataclasses import dataclass

""" Not a Pydantic but it is a simple dataclass. I did not raise errors, printed the error messages instead for better UI/UX."""


@dataclass
class Book:
    _title: str
    _author: str
    _release_date: int
    _num_of_pages: int
    _is_ad: bool = False
    _category: str = "General"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.title}, {self.author}, {self.release_date}, {self.num_of_pages})"

    def __str__(self) -> str:
        return f"{self.title},{self.author},{self.release_date},{self.num_of_pages}"

    @property
    def title(self):
        try:
            return str(self._title)
        except ValueError as e:
            print("(X) ->", e)

    @property
    def author(self):
        try:
            return str(self._author)
        except ValueError as e:
            print("(X) ->", e)

    @property
    def release_date(self):
        try:
            return int(self._release_date)
        except ValueError as e:
            print("(X) ->", e)

    @property
    def num_of_pages(self):
        try:
            return int(self._num_of_pages)
        except ValueError as e:
            print("(X) ->", e)

    # Anno Domini
    @property
    def is_ad(self):
        if self.release_date < 0:
            return True
        return False

    @property
    def category(self):
        return self._category

    def is_valid(self):
        if (
            not self.title
            or not self.author
            or not self.release_date
            or not self.num_of_pages
        ):
            return False
        return True
