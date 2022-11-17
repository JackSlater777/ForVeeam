import os
import shutil
from pathlib import Path
from settings import source_path, replica_path


class Folder:
    """Класс, описывающий папку - источник или реплику."""
    def __init__(self, path: Path):
        self.path = path

    def create_folder(self) -> None:
        """Метод создания папки - для источника."""
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def delete_folder(self) -> None:
        """Метод удаления папки - для реплики перед копированием."""
        if os.path.exists(self.path):
            shutil.rmtree(self.path)


if __name__ == '__main__':
    # Создаем экземпляры источника и реплики
    source = Folder(source_path)
    replica = Folder(replica_path)
    # Создаем папку источника
    source.create_folder()
    # Удаляем папку реплики - в ней не будет ничего лишнего
    replica.delete_folder()
    # Копируем папки
    shutil.copytree(source.path, replica.path)
