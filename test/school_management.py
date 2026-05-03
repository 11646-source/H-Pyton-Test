#!/usr/bin/env python3

from abc import ABC


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} ({})" .format(self.name, self.age)

    def to_dict(self) -> dict:
        return {
                "name": self.name
                "age": self.age
                "type": self.__class__.__name__
                }
        def save_item_data(item: Person) -> None:
            filename = f"{item.name}_{item.age}.json"

            with open(filename, "w", encoding="utf-8") as file:
                json.dump(item.to_dict(), file)
