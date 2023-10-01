import os
from colorama import Fore, Back, Style

# Reading variables from env
text_to_print = os.environ.get("TEXT_TO_PRINT")
number_to_print = os.environ.get("NUMBER_TO_PRINT")

# printing colored output to stdout
print(f"{Fore.RED}TEXT{Style.RESET_ALL}   ==> {Back.BLUE} {text_to_print} {Style.RESET_ALL}")
print(f"{Fore.RED}NUMBER{Style.RESET_ALL} ==> {Back.BLUE} {number_to_print} {Style.RESET_ALL}")
