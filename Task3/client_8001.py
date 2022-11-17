import socket
import pickle
from client_8000 import unique_identifier, unique_code


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 8001
    s.connect((host, port))  # Подключаемся к серверу
    text_message = "text message"  # Генерируем текстовое сообщение
    data = [text_message, unique_identifier, unique_code]  # Формируем список из текстового сообщения, уникального идентификатора и уникального кода
    print(f"Data to send: {data}")
    s.send(pickle.dumps(data))  # Отправляем на сервер текстовое сообщение, уникальный идентификатор и уникальный код
    msg_from_server = s.recv(1024)  # Получаем сообщение от сервера
    print(f"{msg_from_server}")  # Принтим сообщение от сервера
    s.close()
