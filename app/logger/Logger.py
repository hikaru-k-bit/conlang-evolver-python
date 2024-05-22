import colorama


class Logger:
    @staticmethod
    def info(message):
        print(f"{colorama.Fore.GREEN}[INFO] {message}{colorama.Style.RESET_ALL}")

    @staticmethod
    def error(message):
        print(f"{colorama.Fore.RED}[ERROR] {message}{colorama.Style.RESET_ALL}")

    @staticmethod
    def warning(message):
        print(f"{colorama.Fore.YELLOW}[WARNING] {message}{colorama.Style.RESET_ALL}")

    @staticmethod
    def changes_made(message):
        print(f"{colorama.Fore.BLUE}[CHANGES] {message}{colorama.Style.RESET_ALL}")
