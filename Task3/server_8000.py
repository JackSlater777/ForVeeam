import socket
import random


def generate_unique_code(strn):
    """
    Генерируем уникальный код
    """
    # # Формируем словарь под генерацию
    # d1 = {'1': '0', '2': '9', '3': '8', '4': '7', '5': '6', '6': '5', '7': '4', '8': '3', '9': '2', '0': '1'}
    # # Создаем новую строку под уникальный код
    # s_new = ''
    # # Декодируем уникальный идентификатор
    # i = 0
    # while i < len(strn):
    #     if strn[i] in d1:
    #         s_new += d1[strn[i]]
    #     i += 1

    # Рандомим число
    num = random.randint(0, 1)
    # Коинфлип - в 50% случаях идентификатор будет совпадать с кодом
    if num == 0:
        s_new = "10000"
        return s_new
    elif num == 1:
        s_new = strn
        return s_new


if __name__ == '__main__':
    # для сервера
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = '127.0.0.1'
        port = 8000
        s.bind((host, port))  # привязывает адрес (имя хоста, номер порта) к сокету
        s.listen(50)  # Открываем порт на сервере (не более 50 клиентов одновременно)
        while True:
            conn, addr = s.accept()  # Новый сокет для взаимодействия с новым клиентом (переводим в отдельное окно)
            st = conn.recv(1024).decode()  # Получаем уникальный идентификатор от клиента
            conn.send(generate_unique_code(st).encode())  # Отправляем уникальный код клиенту
            conn.close()
