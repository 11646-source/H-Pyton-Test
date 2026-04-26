#!/usr/bin/env python3

from abc import ABC


class LibraryItem(ABC):
    def __init__(self, title, creator, year):
        self.title = title
        self.creator = creator
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.creator} ({self.year})"

    def to_dict(self) -> dict:
        return {
                "title": self.title,
                "creator": self.creator,
                "year": self.year,
                "type": self.__class__.__name__
             }
