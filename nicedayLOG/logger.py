from datetime import datetime
from colorama import Fore

class Output:
    def __init__(self, level):
        self.level = level
        self.color_map = {
            "INFO": (Fore.LIGHTBLUE_EX, "*"),
            "INFO2": (Fore.LIGHTCYAN_EX, "^"),
            "ERROR": (Fore.LIGHTRED_EX, "!"),
            "SUCCESS": (Fore.LIGHTGREEN_EX, "$"),
            "INPUT": (Fore.LIGHTBLACK_EX, "?")
        }

    def log(self, *args, **kwargs):
        color, text = self.color_map.get(self.level, (Fore.LIGHTWHITE_EX, self.level))
        time_now = datetime.now().strftime("%H:%M:%S")

        base = f"[{Fore.LIGHTBLACK_EX}{time_now}{Fore.RESET}] ({color}{text.upper()}{Fore.RESET})"
        for arg in args:
            base += f"{Fore.RESET} {arg}"
        if kwargs:
            base += f"{Fore.RESET} {arg}"

        print(base)

