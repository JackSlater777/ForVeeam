from datetime import datetime


def fill_logs(ms):
    """
    Вносит отметки о копировании файлов в файл logs.txt
    """
    log = "logs.txt"
    now = datetime.now()  # Сейчас
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")  # Конвертируем дату в нужный формат
    if log:
        with open(log, 'a') as f:  # Открываем на дозапись; если файла не существует - создается новый
            f.write(f'{date_time}: {ms}\n')  # Записываем в logs.txt
            print(f'{date_time}: {ms}\n')  # Выводим в консоли
    else:
        with open(log, 'w') as f:  # Открываем на запись; если файла не существует - создается новый
            f.write(f'{date_time}: {ms}\n')  # Записываем в logs.txt
            print(f'{date_time}: {ms}\n')  # Выводим в консоли


if __name__ == '__main__':
    msg = "Hello"
    fill_logs(msg)
