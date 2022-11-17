from datetime import datetime
from pathlib import Path
from settings import source_path, replica_path
from command_arguments import get_command_arguments


class ChangelogStorage:
    """Интерфейс для хранилища любого типа - сохраняем историю бэкапа."""
    def save(self, path: str) -> None:
        raise NotImplementedError


# class PlainFileChangelogStorage(ChangelogStorage):
class PlainFileChangelogStorage:
    """Класс для текстового файла."""
    def __init__(self, path: str):
        self.path = path

    def save(self, s: Path, r: Path) -> None:
        """Вносим историю бэкапа в текстовый файл."""
        now = datetime.now()  # Сейчас
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")  # Конвертируем дату в нужный формат
        with open(self.path, 'a') as f:  # Открываем на дозапись; если файла не существует - создается новый
            f.write(f'{date_time}: Files and folders from {s} are coppied to {r}\n')  # Записываем в logs.txt
            print(f'\n{date_time}: Files and folders from {s} are coppied to {r}\n')  # Выводим в консоли


if __name__ == '__main__':
    # Парсим аргументы из командной строки
    command_arguments = get_command_arguments()
    # Создаем экземпляр лог-файла
    plain_file_changelog_storage = PlainFileChangelogStorage(command_arguments.logfile_name)
    # Вносим информацию о времени бэкапа
    plain_file_changelog_storage.save(source_path, replica_path)
