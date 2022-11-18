import time
from command_arguments import get_command_arguments
from copying_files import copying_process
from history import logging_process


# path:  cd C:\Users\Иван\PycharmProjects\ForVeeam\Task2
# cmd string:  python main.py 5 logs.txt


def cycle() -> int:
    """Главная функция - процесс цикла копирования и логирования."""
    # Запускаем процесс записи истории копирования в файлы
    logging_process()
    # Запускаем процесс копирования
    copying_process()
    # Красивый принт в консоли про окончание копирования
    print("The synchronization cycle has been completed!\n")
    print("*********************************************")
    # Возвращаем межинтервальное время в секундах
    return int(get_command_arguments().recycling_time)


if __name__ == '__main__':
    while True:
        # Выполняем цикл синхронизации, возвращаем межинтервальное время
        recycling_time = cycle()
        # Ждем интервал между циклами в секундах
        time.sleep(recycling_time)

    # # Для теста одного цикла
    # cycle()
