#!/usr/bin/env python3

from abc import ABC
import json

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

def save_item_data(item: LibraryItem) -> None:
    filename = f"{item.title}_{item.creator}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(item.to_dict(), file)
