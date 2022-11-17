from dataclasses import dataclass


@dataclass
class CommandArguments:
    """Класс для описания параметров коммандной строки."""
    python_script_name: str
    recycling_time: str
    logfile_name: str
