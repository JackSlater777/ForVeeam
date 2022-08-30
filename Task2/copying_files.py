import sys
import os
import shutil
from command_arguments import receiving_command_arguments
from fill_logs import fill_logs_copy, fill_logs_delete

# link to the repo: https://github.com/JackSlater777/ForVeeam.git


# path:  cd C:\Users\Иван\PycharmProjects\ForVeeam\Task2
# cmd string:  python copying_files.py 120 logs.txt


def copyfile(src, dest):
    """
    Пофайловое копирование
    """
    with open(src) as f:
        s = f.read()  # Переносим текст файла в переменную, выбрасывает исключение, если такого файла нет
        with open(dest, 'w') as g:  # Открываем на запись
            g.write(s)  # Записываем текст из переменной в destination


def copydir(s, d, log):
    """
    Копирование папки
    """
    # Если destination не существует
    if not os.path.exists(d):
        os.mkdir(d)  # создаем каталог с именем d
    # Если destination существует
    if os.path.exists(d):
        # Пофайлово применяем функцию copyfile
        files = os.listdir(s)  # возвращаем список, содержащий имена файлов и директорий в каталоге s
        for file in files:
            fl = os.path.join(s, file)  # формируем путь файла для копирования
            fl_copy = os.path.join(d, file)  # формируем путь файла под копирование
            # Проверяем, является ли объект файлом
            if os.path.isfile(fl):
                copyfile(fl, fl_copy)  # Выполняем функцию копирования
                fill_logs_copy(fl, fl_copy, log)  # Вносим информацию о копировании в файл logs.txt
            # Проверяем, является ли объект подпапкой
            elif os.path.isdir(fl):
                if not os.path.exists(fl_copy):
                    os.mkdir(fl_copy)  # создаем подпапку под копирование
                copydir(fl, fl_copy, log)  # Делаем рекурсию на копирование папки


def delete(s, d, log):
    """
    Удаление файлов и папок из replica, которых нет в source
    """
    # Пофайлово применяем функцию deletefile для файлов, которые есть в replica, но нет в source
    copied_files = os.listdir(d)  # возвращаем список, содержащий имена файлов и директорий в каталоге d
    for file in copied_files:
        fl = os.path.join(s, file)  # формируем путь файла replica
        fl_copy = os.path.join(d, file)  # формируем путь файла source для сравнения
        # # Проверяем, является ли объект файлом
        if os.path.isfile(fl_copy):
            # Проверяем, существует ли файл в оригинальной папке
            if not os.path.exists(fl):
                os.remove(fl_copy)  # Удаляем файл из replica
                fill_logs_delete(fl_copy, log)  # Вносим информацию об удалении в файл logs.txt
        # Проверяем, является ли объект подпапкой
        elif os.path.isdir(fl_copy):
            # Проверяем, существует ли папка в оригинальной папке
            if os.path.exists(fl):
                delete(fl, fl_copy, log)  # Делаем рекурсию на подпапку
            else:
                shutil.rmtree(fl_copy, ignore_errors=True)  # Удаляем папку из replica с файлами
                fill_logs_delete(fl_copy, log)  # Вносим информацию об удалении в файл logs.txt


if __name__ == '__main__':
    receiving_command_arguments()
    source = r'.\source'
    destination = r'.\replica'
    copydir(source, destination, sys.argv[2])
    delete(source, destination, sys.argv[2])
