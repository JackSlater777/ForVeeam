import socket
import random


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 8000
    s.connect((host, port))  # Подключаемся к серверу
    unique_identifier = str(random.randint(0, 9999))  # Генерируем уникальный идентификатор
    s.send(unique_identifier.encode())  # Отправляем на сервер уникальный идентификатор
    unique_code = s.recv(1024)  # Получаем уникальный код от сервера (1024 байта - размер буфера для данных)
    print(f"Your unique code: {unique_code.decode()}")  # Принтим уникальный код
    s.close()
