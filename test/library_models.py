#!/usr/bin/env python3

from library_management import LibraryItem


class Book(LibraryItem):
    def __init__(self, title, creator, year, pages):
        super().__init__(title, creator, year)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()} - Pages: {self.pages}"
