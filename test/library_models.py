#!/usr/bin/env python3

from library_management import LibraryItem


class Book(LibraryItem):
    def __init__(self, title, creator, year, pages):
        super().__init__(title, creator, year)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()} - Pages: {self.pages}"

 class Movie(LibraryItem):
        def __init__(self, title, creator, year, duration):
            super().__init__(title, creator, year)
            self.duration = duration

        def __str__(self):
            return f"{super().__str__()} - Duration: {self.duration}"

      class MusicAlbum(LibraryItem):
            def __init__(self, title, creator, year, artist):
                super().__init__(title, creator, year)
                self.artist = artist

            def __str__(self):
                return f"{super().__str__()} - Artist: {self.artist}"
