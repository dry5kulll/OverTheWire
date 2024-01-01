import requests
import re
import html
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style
import base64
import binascii

colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

username = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'

url = f'http://{username}.natas.labs.overthewire.org/'

rep_list = {'<br/>': '\n', '&nbsp;': ' ', '&amp;': '&'}


# Decrypt the Secret key
def encodeSecret(secret):
    return base64.b64decode(binascii.unhexlify(secret.encode())[::-1]).decode()


def beautify(resp):
    soup = BeautifulSoup(html.unescape(resp.text), 'lxml')

    for key, value in rep_list.items():
        soup = re.sub(key, value, str(soup))

    return BeautifulSoup(soup, 'lxml')


# Step 1: Grab the Encode Secret from the source code page & decode it to find the key
resp = requests.post(url=url + "index-source.html", auth=(username, password))

soup = beautify(resp)

# Fetching the Encoded Secret from the source code page
encodedSecret = re.search('"(.*)";', soup.text).group(1)
key = encodeSecret(encodedSecret)

data = {"secret": key, "submit": "Whatever you want!!!"}


# Step 2: Use the decrypted key as input to get the password for the next level
resp = requests.post(url=url, auth=(username, password), data=data)
soup = beautify(resp)

print(re.findall('Access granted. (.*)', soup.text)[0])
