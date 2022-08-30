import sys
import time
from command_arguments import receiving_command_arguments
from copying_files import copydir, delete


# path:  cd C:\Users\Иван\PycharmProjects\ForVeeam\Task2
# cmd string:  python run.py 60 logs.txt

def sync():
    copydir(source, destination, sys.argv[2])
    delete(source, destination, sys.argv[2])
    print("\nThe synchronization cycle has been completed!\n")
    print("\n*********************************************\n")


if __name__ == '__main__':
    receiving_command_arguments()
    source = r'.\source'
    destination = r'.\replica'
    while True:
        sync()  # Сразу выполняем цикл синхронизации
        time.sleep(int(sys.argv[1]))  # Интервал между циклами (в секундах)
