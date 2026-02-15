from colorama import Fore, Style, init

init(autoreset=True)

def log_error(message):
    print(f"{Fore.RED} [ERROR] {Fore.RESET} {message}")

def color_file(message):
    return f"{Fore.GREEN}{message}{Style.RESET_ALL}"

def color_dir(message):
    return f"{Fore.CYAN}{message}{Style.RESET_ALL}"

def color_root(message):
    return f"{Fore.YELLOW}{message}{Style.RESET_ALL}"
