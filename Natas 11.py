# Reverse Engineering the source code

import requests
import re
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

rep_list = {'<br/>': '\n', '&nbsp;': ' ', '&amp;': '&'}


# Set the username and password for authentication
username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'

# key = "KNHL"

cookie = {"data": "MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz"}


# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'


# Make a GET request to the URL with basic authentication using the provided credentials & parameters
resp = requests.get(url=url, auth=(username, password), cookies=cookie)


# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(resp.text, 'lxml')


# Extract password for the next level
print(re.search("The password for natas12 is (.*)", soup.text).group(0))
