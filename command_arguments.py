import sys
from schemas import CommandArguments


def get_command_arguments() -> CommandArguments:
    """Функция для валидации аргументов командной строки по датаклассу."""
    print("\nTotal arguments passed:", len(sys.argv))
    # The command line arguments are:
    print(f'\nThe command line arguments are:{sys.argv}')
    # Arguments passed
    print("\nName of Python script:", sys.argv[0])
    print("\nRecycling Time:", sys.argv[1], "sec")
    print("\nName of the History Storage File:", sys.argv[2])

    return CommandArguments(**
                            {
                                "python_script_name": sys.argv[0],
                                "recycling_time": sys.argv[1],
                                "logfile_name": sys.argv[2]
                            })

    # # Mock - для тестирования
    # return CommandArguments(**
    #                         {
    #                             "python_script_name": "main.py",
    #                             "recycling_time": "6",
    #                             "logfile_name": "logs.txt"
    #                         })


if __name__ == '__main__':
    get_command_arguments()
