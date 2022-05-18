import requests
from pprint import pprint

reqUrl = "https://api.github.com/users/georgethomas-liberty/repos"

headersList = {
    "Accept": "*/*",
}

payload = {"name": "new-test-repo"}

# response = requests.get(reqUrl).json()
response = requests.request("POST", reqUrl, data=payload, headers=headersList)

# pprint(response)
print(response.text)
