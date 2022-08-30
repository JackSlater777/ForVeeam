import sys
import os
from datetime import datetime
from command_arguments import receiving_command_arguments


def fill_logs_copy(src, dest, log):
    """
    Вносит отметки о копировании файлов в файл logs.txt
    """
    now = datetime.now()  # Сейчас
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")  # Конвертируем дату в нужный формат
    if log:
        with open(log, 'a') as f:  # Открываем на дозапись; если файла не существует - создается новый
            f.write(f'{date_time}: {src} is coppied to {dest}\n')  # Записываем в logs.txt
            print(f'{date_time}: {src} is coppied to {dest}\n')  # Выводим в консоли
    else:
        with open(log, 'w') as f:  # Открываем на запись; если файла не существует - создается новый
            f.write(f'{date_time}: {src} is coppied to {dest}\n')  # Записываем в logs.txt
            print(f'{date_time}: {src} is coppied to {dest}\n')  # Выводим в консоли


def fill_logs_delete(dest, log):
    """
    Вносит отметки об удалении файлов в файл logs.txt
    """
    now = datetime.now()  # Сейчас
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")  # Конвертируем дату в нужный формат
    if log:
        with open(log, 'a') as f:  # Открываем на дозапись; если файла не существует - создается новый
            f.write(f'{date_time}: {dest} is deleted\n')  # Записываем в logs.txt
            print(f'{date_time}: {dest} is deleted\n')  # Выводим в консоли
    else:
        with open(log, 'w') as f:  # Открываем на запись; если файла не существует - создается новый
            f.write(f'{date_time}: {dest} is deleted\n')  # Записываем в logs.txt
            print(f'{date_time}: {dest} is deleted\n')  # Выводим в консоли


if __name__ == '__main__':
    receiving_command_arguments()
