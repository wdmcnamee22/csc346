import requests
import passwords
url = "https://api.github.com/user"
response = requests.get(url, auth=(passwords.USERNAME, passwords.PASSWORD))
print(response.json())
