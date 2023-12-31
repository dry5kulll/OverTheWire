import requests
import re
import html
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style

colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

rep_list = {'<br/>': '\n', '&nbsp;': ' ', '&amp;': '&'}

username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'
data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "What Ever itr can be"}

url = f'http://{username}.natas.labs.overthewire.org/'

resp = requests.post(url=url, auth=(username, password), data=data)

soup = BeautifulSoup(html.unescape(resp.text), 'lxml')
for key, value in rep_list.items():
    soup = re.sub(key, value, str(soup))

soup = BeautifulSoup(soup, 'lxml')

print(re.findall('Access granted. (.*)', soup.text)[0])
