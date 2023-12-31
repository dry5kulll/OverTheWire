# Sensitive information disclosure in the source code

import requests
import re
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style

colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

username = 'natas0'
password = username

url = f'http://{username}.natas.labs.overthewire.org'

resp = requests.get(url=url, auth=(username, password))

soup = BeautifulSoup(resp.text, 'lxml')
# print(soup.prettify())
# print(soup)
print(re.findall('<!--(.*) -->', resp.text)[-1])
