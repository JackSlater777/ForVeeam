import socket
import pickle
from fill_logs import fill_logs


def check_identifier_and_code(msg, id, code):
    """
    Проверяем соответствие уникального идентификатора и уникального кода
    """
    if id == code:
        fill_logs(msg)
        message = "Your text message has been added to logs"
        return message
    else:
        error_message = "Error!"
        return error_message


if __name__ == '__main__':
    # для сервера
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = '127.0.0.1'
        port = 8001
        s.bind((host, port))  # привязывает адрес (имя хоста, номер порта) к сокету
        s.listen(50)  # Открываем порт на сервере (не более 50 клиентов одновременно)
        while True:
            conn, addr = s.accept()  # Новый сокет для взаимодействия с новым клиентом (переводим в отдельное окно)
            data = pickle.loads(conn.recv(4096))  # Получаем дату от клиента
            check_identifier_and_code(data[0], data[1], data[2])  # Проверяем соответствие уникального идентификатора и уникального кода
            # conn.send(pickle.dumps(data))  # Отправляем обратно клиенту
            conn.send(check_identifier_and_code(data[0], data[1], data[2]).encode())  # Проверяем соответствие уникального идентификатора и уникального кода и отправляем уникальный код клиенту
            conn.close()
