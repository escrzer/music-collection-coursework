class Track:
    """
    Класс трека.
    """

    def __init__(self, title: str, artist: str, duration: int):
        """
            :param title: название трека
            :param artist: имя исполнителя
            :param duration: длительность в секундах
        """
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self) -> str:
        mins = self.duration // 60
        secs = self.duration % 60
        return f"{self.title} — {self.artist} ({mins}:{secs:02d})"
