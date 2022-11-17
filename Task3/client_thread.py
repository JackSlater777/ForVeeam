# Класс потока под клиента
import threading


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):  # Метод для работы с наследниками класса threading.Thread
        print(f'Connection from address {self._address}')
        data = self._connection.recv(1024)
        print(f'Received {data.decode()}')
        self._connection.send(data)
        self._connection.close()
        print(f'Closed connection from {self._address}')
