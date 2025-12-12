from typing import List
from .traсk import Track


class Artist:
    """
    Класс исполнителя.
    """
    def __init__(self, name: str):
        """
        :param name: имя исполнителя
        :param tracks: список треков исполнителя
        """
        self.name = name
        self.tracks: List[Track] = []

    def add_track(self, track: Track) -> None:
        """Добавить трек исполнителю."""
        self.tracks.append(track)

    def remove_track(self, title: str) -> None:
        """Удалить трек по названию."""
        self.tracks = [t for t in self.tracks if t.title != title]

    def list_tracks(self) -> list[Track]:
        """Вернуть список всех треков исполнителя.
        :return self.tracks: Все треки исполнителя"""
        return self.tracks