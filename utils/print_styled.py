from pprint import pprint
from colorama import Fore, Style

def print_debug(content):
    print(Fore.LIGHTBLUE_EX + Style.DIM)
    pprint(content)
    print(Style.RESET_ALL)

def print_verbose(content):
    print(Style.DIM + content + Style.RESET_ALL)

def print_error(content):
    print(Fore.RED + Style.BRIGHT + content + Style.RESET_ALL)

def print_warning(content):
    print(Fore.YELLOW + content + Style.RESET_ALL)

def print_response(content):
    print(Fore.GREEN + content + Style.RESET_ALL)
