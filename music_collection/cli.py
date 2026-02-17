from .track import Track
from .playlist import Playlist


def main():
    """
    Меню управления плейлистом.
    """

    print("Музыкальная коллекция")

    name = input("Введите название плейлиста (Enter — 'Мой плейлист'): ").strip()
    if not name:
        name = "Мой плейлист"

    playlist = Playlist(name)

    while True:
        print("\nМеню:")
        print("1. Показать плейлист")
        print("2. Добавить трек")
        print("3. Найти треки по исполнителю")
        print("4. Перемешать плейлист")
        print("5. Удалить трек по названию")
        print("0. Выход")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            # показать плейлист
            print()
            print(playlist)

        elif choice == "2":
            # добавить трек
            title = input("Название трека: ").strip()
            artist = input("Исполнитель: ").strip()
            duration_str = input("Длительность (в секундах): ").strip()

            try:
                duration = int(duration_str)
            except ValueError:
                print("Ошибка: длительность должна быть числом.")
                continue

            track = Track(title, artist, duration)
            playlist.add_track(track)
            print(f"Трек '{title}' добавлен.")

        elif choice == "3":
            # поиск по исполнителю
            artist_name = input("Имя исполнителя для поиска: ").strip()
            found = playlist.find_by_artist(artist_name)

            if not found:
                print(f"Треков исполнителя '{artist_name}' не найдено.")
            else:
                print(f"Треки исполнителя {artist_name}:")
                for t in found:
                    print(" -", t)

        elif choice == "4":
            # перемешать плейлист
            playlist.shuffle()
            print("Плейлист перемешан.")
            print(playlist)

        elif choice == "5":
            # удалить трек
            title = input("Название трека для удаления: ").strip()
            before = len(playlist.tracks)
            playlist.remove_track(title)
            after = len(playlist.tracks)

            if before == after:
                print(f"Трек с названием '{title}' не найден.")
            else:
                print(f"Трек '{title}' удалён.")

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неизвестный пункт меню, попробуйте ещё раз.")


if __name__ == "__main__":
    main()
