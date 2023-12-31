import requests
import re
import colorama
from colorama import Fore, Style

colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

username = 'natas1'
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'

url = f'http://{username}.natas.labs.overthewire.org'

resp = requests.get(url=url, auth=(username, password))

print(re.findall('<!--(.*) -->', resp.text)[-1])


