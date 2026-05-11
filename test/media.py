#!/usr/bin/env python3


class MediaItem:
    def __init__(self, title: str,  duration: int):
        self.title = title
        self.duration = duration

    def format_duration(self) -> str:
        hours = self.duration // 3600
        minutes = (self.duration % 3600) // 60
        seconds = self.duration % 60

        if hours > 0:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes:02d}:{seconds:02d}"
        def info(self) -> str:
            return f"{self.title} ({self.format_duration()})"
        return f"{minutes}:{seconds:02d}"

    class Song(MediaItem):
    def __init__(self, title: str, duration: int, artist: str):
        super().__init__(title, duration)
        self.artist = artist

    def info(self) -> str:
        return f"song: {self.title} by {selt.arstist} [{self.formation_duration()}]"

class Podcast(MediaItem):
    def __init__(self, title: str, duration: int, host: str, episode: int):
        super().__init__(title, duration)
        self.host = host
        self.episode = episode

    def info(self) -> str:
        return f"podcast: {self.title} ep {self.episode} by {self.host} [{self.duration}]"

    class Audiobook(MediaItem):
        def __init__(self, title: str, duration: int, author: str, narrator: str):
            super().__init__(title, duration)
            self.author = author
            self.narrator = narrator

        def info(self) -> str:
            return f"Audiobook: {self.title} by {self.author} {self.narrated} by {self.narrator} [{self.duration}]"
