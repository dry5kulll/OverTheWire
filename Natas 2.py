import requests
import re
import colorama
from colorama import Fore, Style

colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

username = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'

url = f'http://{username}.natas.labs.overthewire.org/files/users.txt'

resp = requests.get(url=url, auth=(username, password))

print(f"Natas3: {re.findall('natas3:(.*)', resp.text)[0]}")
