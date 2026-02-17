from typing import List
from .track import Track
import random


class Playlist:
    """
    Класс плейлиста.

    :param name: название плейлиста
    :param tracks: список треков в плейлисте
    """

    def __init__(self, name: str):
        self.name = name
        self.tracks: List[Track] = []

    def add_track(self, track: Track) -> None:
        """Добавить трек в плейлист."""
        self.tracks.append(track)

    def remove_track(self, title: str) -> None:
        """Удалить трек по названию."""
        self.tracks = [t for t in self.tracks if t.title != title]

    def find_by_artist(self, artist_name: str) -> List[Track]:
        """
        Поиск треков по исполнителю.

         :param artist_name: имя исполнителя
        :type artist_name: str
        :return: список треков данного исполнителя
        :rtype: List[Track]
        """
        return [t for t in self.tracks if t.artist == artist_name]

    def shuffle(self) -> None:
        """Перемешать плейлист."""
        random.shuffle(self.tracks)

    def __str__(self) -> str:
        """
        Строковое представление плейлиста.

        :return: многострочная строка со списком треков
        :rtype: str
        """
        if not self.tracks:
            return f"Плейлист: {self.name}\n(пока нет треков)"

        lines = [f"Плейлист: {self.name}"]
        for i, track in enumerate(self.tracks, start=1):
            lines.append(f"{i}. {track}")
        return "\n".join(lines)

if __name__ == "__main__":
    ...
