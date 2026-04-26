#!/usr/bin/env python3

from abc import ABC


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} ({})" .format(self.name, self.age)
