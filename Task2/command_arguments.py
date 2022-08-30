import sys


# cmd string:  python command_arguments.py 120 logs.txt

def receiving_command_arguments():
    # total arguments
    n = len(sys.argv)
    print("\nTotal arguments passed:", n)

    # Arguments passed
    print("\nName of Python script:", sys.argv[0])

    print(f'\nThe command line arguments are:{sys.argv}\n')
    # for i in sys.argv:
    #     print(i)


if __name__ == '__main__':
    receiving_command_arguments()
