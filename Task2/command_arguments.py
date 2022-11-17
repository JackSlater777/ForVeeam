import sys
from exceptions import IncorrectInputCmdArguments
from schemas import CommandArguments

# cmd string:  python command_arguments.py 60 logs.txt


def get_command_arguments() -> CommandArguments:
    """Функция для валидации аргументов командной строки по датаклассу."""
    n = len(sys.argv)
    print("\nTotal arguments passed:", n)
    if n == 3:
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
    else:
        raise IncorrectInputCmdArguments


if __name__ == '__main__':
    command_arguments = get_command_arguments()
