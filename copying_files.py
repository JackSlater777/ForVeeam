import os
import shutil
from pathlib import Path
from settings import source_path, replica_path


class Folder:
    """Класс, описывающий папку - источник или реплику."""
    def __init__(self, path: Path):
        self.path = path


class Source(Folder):
    """Класс, описывающий папку источника."""
    def __init__(self, path: Path):
        super().__init__(path)
        # Автоматом проверяем наличие источника
        self.create_folder()

    def create_folder(self) -> None:
        """Метод создания папки - для источника."""
        if not os.path.exists(self.path):
            os.mkdir(self.path)


class Replica(Folder):
    """Класс, описывающий папку реплики."""
    def __init__(self, path: Path):
        super().__init__(path)
        # Автоматом удаляем реплику
        self.delete_folder()

    def delete_folder(self) -> None:
        """Метод удаления папки - для реплики перед копированием."""
        if os.path.exists(self.path):
            shutil.rmtree(self.path)


def copying_process() -> None:
    """Процесс копирования источника в реплику."""
    # Создаем экземпляры
    source = Source(source_path)
    replica = Replica(replica_path)
    # Копируем папки
    shutil.copytree(source.path, replica.path)


if __name__ == '__main__':
    copying_process()
