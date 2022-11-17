import time
import shutil
from command_arguments import get_command_arguments
from copying_files import Folder
from history import PlainFileChangelogStorage
from settings import source_path, replica_path


# path:  cd C:\Users\Иван\PycharmProjects\ForVeeam\Task2
# path:  cd C:\Users\Иван\PycharmProjects\ForVeeam\Task2 OOP refactoring
# cmd string:  python main.py 5 logs.txt


def cycle():
    """Главная функция - процесс цикла копирования."""

    # Парсим аргументы из командной строки
    command_arguments = get_command_arguments()
    # Создаем экземпляры источника и реплики
    source = Folder(source_path)
    replica = Folder(replica_path)
    # Создаем папку источника
    source.create_folder()
    # Удаляем папку реплики - в ней не будет ничего лишнего
    replica.delete_folder()
    # Копируем папки
    shutil.copytree(source.path, replica.path)
    # Создаем экземпляр лог-файла
    plain_file_changelog_storage = PlainFileChangelogStorage(command_arguments.logfile_name)
    # Вносим информацию о времени бэкапа
    plain_file_changelog_storage.save(source_path, replica_path)
    # Красивый принт в консоли про окончание копирования
    print("The synchronization cycle has been completed!\n")
    print("*********************************************")
    # Возвращаем межинтервальный цикл в секундах
    return int(command_arguments.recycling_time)


if __name__ == '__main__':
    while True:
        # Выполняем цикл синхронизации, возвращаем межинтервальное время
        recycling_time = cycle()
        # Ждем интервал между циклами (в секундах)
        time.sleep(recycling_time)
