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
        """
        Добавить трек исполнителю.

        :param track: объект трека
        :type track: Track
        :return: None
        :rtype: None
        """
        self.tracks.append(track)

    def remove_track(self, title: str) -> None:
        """
        Удалить трек по названию.

        :param title: название трека для удаления
        :type title: str
        :return: None
        :rtype: None
        """
        self.tracks = [t for t in self.tracks if t.title != title]

    def list_tracks(self) -> list[Track]:
        """
        Вернуть список всех треков исполнителя.

        :return: список треков
        :rtype: List[Track]
        """
        return self.tracks

if __name__ == "__main__":
    ...
