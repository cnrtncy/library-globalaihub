from rich.console import Console
from rich.table import Table

""" A simple class to visualize data in a table format. Based on Rich library."""


class CLITable:
    def __init__(self, title, rows: list = [], columns: list = None, row_style=None):
        self.title = title
        self.rows = rows
        self.table = Table(title=self.title, show_header=True)
        self.row_style = row_style
        self.columns = columns
        self._add_column()
        self._add_row()

    def __repr__(self) -> str:
        return f"{self.title} by -> {self.columns}"

    def _add_column(self):
        for column in self.columns:
            self.table.add_column(column)

    def _add_row(self):
        for row in self.rows:
            self.table.add_row(*row, style=self.row_style)

    def add_row(self, *args, style=None):
        if style is None:
            self.table.add_row(*args)
        else:
            self.table.add_row(*args, style=style)

    def show(self):
        console = Console()
        console.print(self.table)
