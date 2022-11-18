import os
import json
from datetime import datetime
from pathlib import Path
from settings import source_path, replica_path, save_as_json
from command_arguments import get_command_arguments


class ChangelogStorage:
    """Интерфейс для хранилища любого типа - сохраняем историю бэкапа."""
    def __init__(self,  path: str):
        self.path = path

    def save(self, s: Path, r: Path) -> None:
        """Заглушка для типов хранилищ, которые еще не реализованы."""
        raise NotImplementedError


class PlainFileChangelogStorage(ChangelogStorage):
    """Класс для текстового файла."""
    def __init__(self, path: str):
        super().__init__(path)

    def save(self, s: Path, r: Path) -> None:
        """Вносим историю бэкапа в текстовый файл."""
        with open(self.path, 'a') as f:  # Открываем на дозапись; если файла не существует - создается новый
            # Записываем в logs.txt
            f.write(f'{check_and_convert_time()}: Files and folders from {s} are coppied to {r}\n')
            # Выводим в командной строке
            print(f'\n{check_and_convert_time()}: Files and folders from {s} are coppied to {r}\n')


class JSONFileChangelogStorage(ChangelogStorage):
    """Класс для JSON файла."""
    def __init__(self, path: str):
        super().__init__(path)
        # Сразу проверяем существование
        self.init_storage()

    def save(self, s: Path, r: Path) -> None:
        """Вносим историю бэкапа в JSON файл."""
        # Читаем json-файл
        history = self.read_storage()
        # Формируем дату под добавление
        data = {
            "backup_time": check_and_convert_time(),
            "source": s,
            "replica": r
        }
        # Добавляем в список дату
        history.append(data)
        # Сериализуем данные в json-файл
        with open(self.path, 'w') as f:  #
            json.dump(history, f, sort_keys=True, indent=4)

    def init_storage(self) -> None:
        """Создаем пустой json-файл"""
        if not os.path.exists(self.path):
            # Сериализуем пустой список в json-файл
            with open(self.path, 'w') as f:
                json.dump(list(), f, sort_keys=True, indent=4)

    def read_storage(self) -> list:
        """Читаем json-файл."""
        with open(self.path, "r") as f:
            return json.load(f)


def check_and_convert_time() -> str:
    """Устанавливаем текущее время."""
    now = datetime.now()  # Сейчас
    return now.strftime("%m/%d/%Y, %H:%M:%S")  # Конвертируем дату в нужный формат


def create_json_path() -> str:
    """Заменяем txt на json в пути файла."""
    for i in range(len(get_command_arguments().logfile_name)):
        if get_command_arguments().logfile_name[i] == '.':
            json_path = get_command_arguments().logfile_name[:i+1] + 'json'
            return json_path


def logging_process() -> None:
    """Процесс записи истории копирования в файлы."""
    # Создаем экземпляр txt лог-файла
    plain_file_changelog_storage = PlainFileChangelogStorage(get_command_arguments().logfile_name)
    # Вносим информацию о времени бэкапа
    plain_file_changelog_storage.save(source_path, replica_path)
    # Если опция "сохранить в json включена
    if save_as_json:
        # Создаем экземпляр json лог-файла ...
        json_file_changelog_storage = JSONFileChangelogStorage(create_json_path())
        # Вносим информацию о времени бэкапа
        json_file_changelog_storage.save(source_path, replica_path)


if __name__ == '__main__':
    logging_process()
