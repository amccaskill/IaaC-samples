from tkinter import FALSE
import requests
import json
import pprint
# Get token and store in variable "token"
requests.packages.urlib3.disable_warnings()
url = "https://10.10.20.65/api/fdm/v5/fdm/token"

payload =  {"grant_type": "password", "username": "admin", "password":"Cisco1234"}
headers =  {"Accept": "application/json", "Content-type": "application/json"}

token_response = requests.post(
    url, headers=headers, data=json.dump(payload), verify=False
 )
token_response.raise_for_status()
if token_response.status_code == 200:
     print("Token Successfully Received...\n")

token = token_response.json()["access_token"]

# Take token to authenticate, then create object
url = "https://10.10.20.65/api/fdm/v5/object/networks"

payload = {
    "name": "AdrianNet",
    "description": "FTD_TEST",
    "subType": "NETWORK",
    "value": "98.96.97.0/24",
    "dnsResolution": "IPV$_ONLY",
    "type": "networkobject",
}

headers ={
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization":  f"Bearer {token}",
}

create_response = requests.post(
    url, headers=headers, data=json().dumps(payload), verify=False
)
create_response.raise_for_status()
if create_response.raise_for_status == 200:
    print("Successful object creation")
    print(create_response.text)


