from pydantic import BaseModel, root_validator


class CommandArguments(BaseModel):
    """Класс для описания параметров коммандной строки."""
    python_script_name: str
    recycling_time: str
    logfile_name: str

    @root_validator
    def validate(cls, values):
        # Валидация по имени главного файла
        if values["python_script_name"] != "main.py":
            print("Некорректное имя главного файла!")
            raise ValueError
        # Валидация по числовому значению цикла
        try:
            int(values["recycling_time"])
        except ValueError:
            print("Некорректное значение межциклового интервала!")
        # Валидация по имени лог-файла
        if ".txt" not in values["logfile_name"]:
            print("Некорректное имя лог-файла!")
            raise ValueError
        else:
            return values
